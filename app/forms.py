from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(message="Field is Required")])
    password=PasswordField('Password',validators=[DataRequired(message="Field is Required"  )])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('SignIn')