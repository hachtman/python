from flask_wtf import form
from wtfroms import StringField
from wtforms.validators import (DataRequired, Regexp,
                                ValidationError, Email, Length, EqualTo)
from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("A user with the name already exists.")


def email_exists
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
            Length(min=2),
            EqualTo('password2', message="Passwords must match.")
        ]
    )
