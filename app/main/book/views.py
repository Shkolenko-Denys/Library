# -*- coding:utf-8 -*-
from app import db
from app.models import Book, Log, Comment, Permission, Tag, book_tag,\
    Author, Publisher, Genre, Udc
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import current_user
from . import book
from .forms import SearchForm, EditBookForm, AddBookForm
from ..comment.forms import CommentForm
from ..decorators import admin_required, permission_required


@book.route('/')
def index():
    """Search by search_word in Book fields using SearchForm."""
    search_word = request.args.get('search', None)
    search_form = SearchForm()
    page = request.args.get('page', 1, type=int)

    the_books = Book.query
    if not current_user.can(Permission.UPDATE_BOOK_INFORMATION):
        the_books = Book.query.filter_by(hidden=0)

    if search_word:
        search_word = search_word.strip()
        the_books = the_books.filter(db.or_(
            Book.title.ilike(u"%%%s%%" % search_word),
            Book.author.surnames_initials.ilike(u"%%%s%%" % search_word),
            Book.genre.genre.ilike(u"%%%s%%" % search_word),
            Book.publisher.publisher.ilike(u"%%%s%%" % search_word),
            Book.isbn.ilike(u"%%%s%%" % search_word),
            Book.tags.any(Tag.name.ilike(u"%%%s%%" % search_word))))\
            .outerjoin(Log).group_by(Book.id)\
            .order_by(db.func.count(Log.id).desc())
        search_form.search.data = search_word
    else:
        the_books = Book.query.order_by(Book.id.desc())

    pagination = the_books.paginate(page, per_page=8)
    result_books = pagination.items
    return render_template("book.html", books=result_books,
                           pagination=pagination, search_form=search_form,
                           title=u"List of Books")


@book.route('/<book_id>/')
def detail(book_id):
    """Get details of the book by book_id."""
    the_book = Book.query.get_or_404(book_id)

    if the_book.hidden and (not current_user.is_authenticated or
                            not current_user.is_administrator()):
        abort(404)

    show = request.args.get('show', 0, type=int)
    page = request.args.get('page', 1, type=int)
    form = CommentForm()

    if show in (1, 2):
        pagination = the_book.logs.filter_by(returned=show-1) \
            .order_by(Log.borrow_timestamp.desc()).paginate(page, per_page=5)
    else:
        pagination = the_book.comments.filter_by(deleted=0) \
            .order_by(Comment.edit_timestamp.desc()).paginate(page, per_page=5)

    data = pagination.items
    return render_template("book_detail.html", book=the_book, data=data,
                           pagination=pagination, form=form,
                           title=the_book.title)


@book.route('/<int:book_id>/edit/', methods=['GET', 'POST'])
@permission_required(Permission.UPDATE_BOOK_INFORMATION)
def edit(book_id):
    """Edit book fields using EditBookForm."""
    book = Book.query.get_or_404(book_id)
    form = EditBookForm()
    if form.validate_on_submit():
        new_author = Author(surnames_initials=form.author.data)
        new_publisher = Publisher(publisher=form.publisher.data)
        new_genre = Genre(genre=form.genre.data)
        new_udc = Udc(udc_number=form.udc.data)

        book.title = form.title.data
        book.author_id = new_author.id
        book.publisher_id = new_publisher.id
        book.genre_id = new_genre.id
        book.udc_id = new_udc.id
        book.isbn = form.isbn.data
        book.image = form.image.data
        book.pub_year = form.pub_year.data
        book.tags_string = form.tags.data
        book.numbers = form.numbers.data
        book.summary = form.summary.data
        book.catalog = form.catalog.data

        book.author = new_author
        book.publisher = new_publisher
        book.genre = new_genre
        book.udc = new_udc

        db.session.add_all([book, new_author, new_publisher, new_genre, new_udc])
        db.session.commit()
        flash(u'Book data has been saved!', 'success')
        return redirect(url_for('book.detail', book_id=book_id))
    form.title.data = book.title
    form.author = Author(surnames_initials=book.author)
    form.publisher = Publisher(publisher=book.publisher)
    form.genre = Genre(genre=book.genre)
    form.udc = Udc(udc_number=book.udc)
    form.isbn.data = book.isbn
    form.image.data = book.image
    form.pub_year.data = book.pub_year
    form.tags.data = book.tags_string
    form.numbers.data = book.numbers
    form.summary.data = book.summary or ""
    form.catalog.data = book.catalog or ""
    return render_template("book_edit.html", form=form, book=book,
                           title=u"Edit book information")


@book.route('/add/', methods=['GET', 'POST'])
@permission_required(Permission.ADD_BOOK)
def add():
    """Add book using AddBookForm."""
    form = AddBookForm()
    form.numbers.data = 3
    if form.validate_on_submit():
        new_author = Author(surnames_initials=form.author.data)
        new_publisher = Publisher(publisher=form.publisher.data)
        new_genre = Genre(genre=form.genre.data)
        new_udc = Udc(udc_number=form.udc.data)
        new_book = Book(
            new_author, new_publisher, new_genre, new_udc,
            title=form.title.data,
            isbn=form.isbn.data,
            image=form.image.data,
            pub_year=form.pub_year.data,
            tags_string=form.tags.data,
            numbers=form.numbers.data,
            summary=form.summary.data or "",
            catalog=form.catalog.data or "")
        new_book.author_id = new_author.id
        new_book.publisher_id = new_publisher.id
        new_book.genre_id = new_genre.id
        new_book.udc_id = new_udc.id

        new_book.author = new_author
        new_book.publisher = new_publisher
        new_book.genre = new_genre
        new_book.udc = new_udc

        db.session.add_all([new_book, new_author, new_publisher, new_genre, new_udc])
        db.session.commit()
        flash(u'Book %s has been added to the library!' % new_book.title,
              'success')
        return redirect(url_for('book.detail', book_id=new_book.id))
    return render_template("book_edit.html", form=form, title=u"Add new book")


@book.route('/<int:book_id>/delete/')
@permission_required(Permission.DELETE_BOOK)
def delete(book_id):
    """Delete (hide) book by book_id."""
    the_book = Book.query.get_or_404(book_id)
    the_book.hidden = 1
    db.session.add(the_book)
    db.session.commit()
    flash(u'successfully delete the book, '
          u'the user can no longer view the book', 'info')
    return redirect(request.args.get('next') or url_for('book.detail',
                                                        book_id=book_id))


@book.route('/<int:book_id>/put_back/')
@admin_required
def put_back(book_id):
    """Restore the book by book_id."""
    the_book = Book.query.get_or_404(book_id)
    the_book.hidden = 0
    db.session.add(the_book)
    db.session.commit()
    flash(u'Successfully restored the book, the user can now view the book',
          'info')
    return redirect(request.args.get('next') or url_for('book.detail',
                                                        book_id=book_id))


@book.route('/tags/')
def tags():
    search_tags = request.args.get('search', None)
    page = request.args.get('page', 1, type=int)
    the_tags = Tag.query.outerjoin(book_tag)\
        .group_by(book_tag.c.tag_id).order_by(
        db.func.count(book_tag.c.book_id).desc()).limit(30).all()
    search_form = SearchForm()
    search_form.search.data = search_tags

    data = None
    pagination = None

    if search_tags:
        tags_list = [s.strip() for s in search_tags.split(',')
                     if len(s.strip()) > 0]
        if len(tags_list) > 0:
            the_books = Book.query
            if not current_user.can(Permission.UPDATE_BOOK_INFORMATION):
                the_books = Book.query.filter_by(hidden=0)
            the_books = the_books.filter(
                db.and_(*[Book.tags.any(Tag.name.ilike(word))
                          for word in tags_list])).outerjoin(Log).group_by(
                Book.id).order_by(db.func.count(Log.id).desc())
            pagination = the_books.paginate(page, per_page=8)
            data = pagination.items

    return render_template('book_tag.html', tags=the_tags, title='Tags',
                           search_form=search_form, books=data,
                           pagination=pagination)
