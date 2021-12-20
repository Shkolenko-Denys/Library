# -*- coding:utf-8 -*-
from app.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    isbn = StringField(
        u"ISBN", validators=[DataRequired(
            message=u"I forgot to fill in this item!"),
            Regexp('[0-9]{13,13}', message=u"ISBN must be 13 digits")])
    title = StringField(
        u"Book Title", validators=[DataRequired(
            message=u"I forgot to fill in this item!"),
            Length(1, 128, message=u"The length is 1 to 128 characters")])
    origin_title = StringField(
        u"Original name",
        validators=[Length(0, 128,
                           message=u"The length is 0 to 128 characters")])
    subtitle = StringField(
        u"Subtitle",
        validators=[Length(0, 128,
                           message=u"The length is 0 to 128 characters")])
    author = StringField(
        u"Author",
        validators=[Length(0, 128,
                           message=u"The length is 0 to 64 characters")])
    translator = StringField(
        u"Translator",
        validators=[Length(0, 64,
                           message=u"The length is 0 to 64 characters")])
    publisher = StringField(
        u"publisher",
        validators=[Length(0, 64, message=u"length is 0 to 64 characters")])
    image = StringField(
        u"picture address",
        validators=[Length(0, 128, message=u"length is 0 to 128 characters")])
    pubdate = StringField(
        u"Publication Date",
        validators=[Length(0, 32,
                           message=u"The length is 0 to 32 characters")])
    tags = StringField(
        u"label",
        validators=[Length(0, 128, message=u"length is 0 to 128 characters")])
    pages = IntegerField(u"page number")
    price = StringField(
        u"Pricing",
        validators=[Length(0, 64,
                           message=u"The length is 0 to 32 characters")])
    binding = StringField(
        u"binding",
        validators=[Length(0, 16, message=u"length is 0 to 16 characters")])
    numbers = IntegerField(
        u"Collection",
        validators=[DataRequired(message=u"I forgot to fill in this item!")])
    summary = PageDownField(u"Content Introduction")
    catalog = PageDownField(u"catalog")
    submit = SubmitField(u"Save changes")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(
                u'The same ISBN already exists and cannot be entered, please '
                u'check carefully whether the book has been stocked.')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"search")
