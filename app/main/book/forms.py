# -*- coding:utf-8 -*-
from app.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    """Form for editing book fields."""
    title = StringField(
        u"Book Title", validators=[DataRequired(
            message=u"I forgot to fill in this item!"),
            Length(1, 128, message=u"The length is 1 to 128 characters")])
    author = StringField(
        u"Author",
        validators=[Length(0, 128,
                           message=u"The length is 0 to 128 characters")])
    publisher = StringField(
        u"Publisher",
        validators=[Length(0, 128, message=u"The length is 0 to 128 characters")])
    genre = StringField(
        u"Genre",
        validators=[
            Length(0, 128, message=u"The length is 0 to 128 characters")])
    udc = IntegerField(
        u"UDC",
        validators=[DataRequired(message=u"I forgot to fill in this item!")])
    isbn = StringField(
        u"ISBN", validators=[DataRequired(
            message=u"I forgot to fill in this item!"),
            Regexp('\d{13}', message=u"ISBN must be 13 digits")])
    image = StringField(
        u"picture address",
        validators=[Length(0, 128, message=u"length is 0 to 128 characters")])
    pub_year = StringField(
        u"Publication Year", validators=[DataRequired(
            message=u"I forgot to fill in this item!"),
            Regexp('\d{4}', message=u"Year must be 4 digits")])
    tags = StringField(
        u"Tags",
        validators=[Length(0, 128, message=u"The length is 0 to 128 characters")])
    numbers = IntegerField(
        u"Collection",
        validators=[DataRequired(message=u"I forgot to fill in this item!")])
    summary = PageDownField(u"Content Introduction")
    catalog = PageDownField(u"catalog")
    submit = SubmitField(u"Save changes")


class AddBookForm(EditBookForm):
    """Form for adding new book."""
    def validate_isbn(self, filed):
        """Method for checking whether there is the same isbn."""
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(
                u'The same ISBN already exists and cannot be entered, please '
                u'check carefully whether the book has been stocked.')


class SearchForm(FlaskForm):
    """Form for searching book information."""
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"search")
