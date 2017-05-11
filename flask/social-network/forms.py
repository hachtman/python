from flask_wtf import Form
from flas_bcrypt import check_password_hash
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp,
                                ValidationError, Email, Length, EqualTo)
from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("A user with the name already exists.")


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError("A user with the email already exists.")


class RegistrationForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, numbers and underscores only.")
            ),
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8),
            EqualTo('password_confirmation', message="Passwords must match.")
        ])
    password_confirmation = PasswordField(
        'Password Confirmation',
        validators=[DataRequired()])


class LoginForm(Form):
    email = StringField(
        'Email',
        validators=[
            DataRequired()
            Email()
        ]
    )
