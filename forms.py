from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField
import email_validator
from wtforms.validators import Email, Length, InputRequired

class CreateUserForm(FlaskForm):

    username = StringField("Username:", validators=[Length(max=20), InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    email = StringField("Email:", validators=[Length(50), InputRequired(), Email()])
    first_name = StringField("First Name:", validators=[Length(30), InputRequired()])
    last_name = StringField("Last Name:", validators=[Length(30), InputRequired()])

# class LoginForm(FlaskForm):
