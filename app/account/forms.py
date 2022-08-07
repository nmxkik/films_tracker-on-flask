from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
    EmailField,
)
from wtforms.validators import Email, EqualTo, InputRequired, Length, DataRequired

from models.user import User


class LoginForm(FlaskForm):
    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    username = StringField(
        'username', validators=[InputRequired(),
                                  Length(1, 64)])

    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()
                             ]
        )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('Email already registered. (Did you mean to '
                                  '<a href="{}">log in</a> instead?)'.format(
                                    url_for('account.login')))


    def validate_login_name(self, login_name):
        if User.query.filter_by(login=login_name.data).first():
            raise ValidationError("Username already taken!")
