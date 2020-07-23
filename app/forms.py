from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Email,ValidationError
from .models import User


class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(message="Field is Required")])
    password=PasswordField('Password',validators=[DataRequired(message="Field is Required")])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('SignIn')


class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(message="Field is Required")])
    email=StringField('Email',validators=[DataRequired(message="Field is Required")])
    password=PasswordField('Password',validators=[DataRequired(message="Field is Required")])
    password2=PasswordField('Confirm Password',validators=[DataRequired(message="Field is Required"),EqualTo('password')])
    submit=SubmitField('Sign Up')
    
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()

        if user is not None:
            raise ValidationError("Please use a different username")


    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()

        if user is not None:
            raise ValidationError("Please use a valid Email")