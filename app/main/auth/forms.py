# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    """Form for logging in."""
    email = StringField(
        'Email',
        validators=[DataRequired(message=u"I forgot to fill in this item!"),
                    Length(1, 64),
                    Email(message=u"Are you sure this is Email?")])
    password = PasswordField(u'PASSWORD',
                             validators=[DataRequired(
                                 message=u"I forgot to fill in this item!"),
                                 Length(6, 32)])
    remember_me = BooleanField(u"Keep my login status", default=True)
    submit = SubmitField(u'login')


class RegistrationForm(FlaskForm):
    """Form for registration."""
    email = StringField(
        'Email',
        validators=[DataRequired(
            message=u"I forgot to fill in this item!"),
            Length(1, 64),
            Email(message=u"Are you sure this is Email?")])
    name = StringField(
        u'Username',
        validators=[DataRequired(message=u"I forgot to fill in this item!"),
                    Length(1, 64)])
    password = PasswordField(
        u'password',
        validators=[DataRequired(message=u"I forgot to fill in this item!"),
                    EqualTo('password2', message=u'Password must match'),
                    Length(6, 32)])
    password2 = PasswordField(
        u'Reconfirm the password',
        validators=[DataRequired(message=u"I forgot to fill in this item!")])
    submit = SubmitField(u'register')

    def validate_email(self, filed):
        """Method to check if the email is already registered."""
        if User.query.filter(db.func.lower(User.email) ==
                             db.func.lower(filed.data)).first():
            raise ValidationError(u'The Email has already been registered')


class ChangePasswordForm(FlaskForm):
    """Form for changing password."""
    old_password = PasswordField(
        u'old password',
        validators=[DataRequired(message=u"I forgot to fill in this item!")])
    new_password = PasswordField(
        u'new password',
        validators=[DataRequired(message=u"I forgot to fill in this item!"),
                    EqualTo('confirm_password',
                            message=u'password must match'),
                    Length(6, 32)])
    confirm_password = PasswordField(
        u'Confirm new password',
        validators=[DataRequired(message=u"I forgot to fill in this item!")])
    submit = SubmitField(u"Save Password")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'The original password is wrong')
