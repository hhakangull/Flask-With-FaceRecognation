from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', id='username_login', validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])
    login = SubmitField('Login')


class CreateAccountForm(FlaskForm):
    user_TC = StringField('TC NO', id='user_TC_create',
                          validators=[DataRequired(), Length(min=11, message="Kimlik No Hatalı")])
    username = StringField('Kullanıcı Adı', id='username_create', validators=[DataRequired()])
    firstname = StringField('İsim', id='firstname_create', validators=[DataRequired()])
    lastname = StringField('Soyisim', id='lastname_create', validators=[DataRequired()])
    email = StringField('Email', id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Parola', id='pwd_create', validators=[DataRequired(), Length(min=6)])
    register = SubmitField('Register')
