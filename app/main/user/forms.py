# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    """Form for editing user profile."""
    name = StringField(u'Username', validators=[
        DataRequired(message=u"I forgot to fill in this item!"),
        Length(1, 64, message=u"The length is 1 to 64 characters")])
    major = StringField(u'Major', validators=[
        Length(0, 128, message=u"The length is 0 to 128 characters")])
    headline = StringField(u'Introduce yourself in one sentence', validators=[
        Length(0, 32, message=u"The length is within 32 characters")])
    about_me = PageDownField(u"Introduction")
    submit = SubmitField(u"Save changes")


class AvatarEditForm(FlaskForm):
    """Form for editing user avatar."""
    avatar_url = StringField('', validators=[
        Length(1, 100, message=u"The length is limited to 100 characters"),
        URL(message=u"Please fill in the correct URL")])
    submit = SubmitField(u"Save")


class AvatarUploadForm(FlaskForm):
    """Form for uploading user avatar."""
    avatar = FileField('', validators=[
        FileAllowed(avatars, message=u"Only allow uploading pictures")])
