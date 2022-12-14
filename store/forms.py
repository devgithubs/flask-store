from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    emails_address = StringField(label='Email')
    password1 = PasswordField(label='Enter Password')
    password2 = PasswordField(label='Confirm Password')
    submit = SubmitField(label='Create Account')
