# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    """Form for writing book review."""
    comment = TextAreaField(
        u"your book review",
        validators=[DataRequired(message=u"The content cannot be empty"),
                    Length(1, 1024,
                           message=u"The length of book reviews is limited "
                                   u"to 1024 characters")])
    submit = SubmitField(u"Publish")
