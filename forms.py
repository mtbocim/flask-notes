from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
#import email_validator
from wtforms.validators import Email, Length, InputRequired


class CreateUserForm(FlaskForm):
    """Form to create a new user."""

    username = StringField(
        "Username:",
        validators=[
            Length(max=20),
            InputRequired()
        ]
    )

    password = PasswordField(
        "Password:",
        validators=[
            InputRequired()
            #add min/max length
        ]
    )

    email = StringField(
        "Email:",
        validators=[
            Length(max=50),
            InputRequired(),
            Email()
        ]
    )

    first_name = StringField(
        "First Name:",
        validators=[
            Length(max=30),
            InputRequired()
        ]
    )

    last_name = StringField(
        "Last Name:",
        validators=[
            Length(max=30),
            InputRequired()
        ]
    )


class LoginForm(FlaskForm):
    """Form to login a user."""

    username = StringField(
        "Username:",
        validators=[
            Length(max=20),
            InputRequired()
        ]
    )

    password = PasswordField(
        "Password:",
        validators=[
            InputRequired()
        ]
    )


class CSRFProtectForm(FlaskForm):
    """Form for CSRF protection"""
