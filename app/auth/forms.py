# Import Form and RecaptchaField (optional)
from flask_wtf import Form

from wtforms import EmailField, PasswordField 

# Import Form validators
from wtforms.validators import DataRequired, Email, EqualTo, Regexp


# Define the login form (WTForms)

class LoginForm(Form):
    email    = EmailField('Email Address', [Email(),
                DataRequired(message='Forgot your email address?')])

    password = PasswordField('Password', [
                DataRequired(message='Must provide a password. ;-)')])

class SignupForm(Form):

    email       = EmailField('Email Address', [
                                Email(),
                                DataRequired(message='Forgot your email address?')])
    
    password    = PasswordField('Password', [
                                DataRequired(message='Must provide a password. ;-)'),
                                Regexp("(?=^.{8,}$)(?=.*\d)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$",message="Let's use a stronger password, shall we? ;)")])

    repassword  = PasswordField('Repassword', [
                                DataRequired(message='Must provide a password. ;-)'),
                                EqualTo('password',message="Oops, passwords aren't matching!")
                                ])