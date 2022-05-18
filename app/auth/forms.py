from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, 
                    ValidationError, BooleanField)
from wtforms.validators import input_required, Email, EqualTo
from ..models import User

class SignUpForm(FlaskForm):
    first_name = StringField("Your First Name", validators=[input_required()])
    last_name = StringField("Your Last Name", validators=[input_required()])
    username = StringField("Your Username", validators=[input_required()])
    email = StringField("Your Email Address", validators=[input_required(), Email()])
    password = PasswordField("Password", validators=[input_required(),
                             EqualTo("password_confirm", message = "Passwords must match")])
    password_confirm = PasswordField("Confirm Password", validators=[input_required()])
    submit = SubmitField("Sign Up")

    #Custom email validation
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")

    #Custom username validation
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is taken")

class LoginForm(FlaskForm):
    email = StringField("Your Email Address", validators=[input_required(), Email()])
    password = PasswordField("Password", validators=[input_required()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")