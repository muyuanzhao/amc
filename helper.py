# -*- coding: utf-8 -*-

from flask.ext import wtf, login
from flask.ext.admin.base import MenuLink
from model import User
from app import db


# Define login and registration forms (for flask-login)
class LoginForm(wtf.Form):
    login = wtf.TextField(u'用户名', validators=[wtf.required()])
    password = wtf.PasswordField(u'密码', validators=[wtf.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise wtf.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise wtf.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(wtf.Form):
    login = wtf.TextField(u'用户名', validators=[wtf.required()])
    email = wtf.TextField(u'邮箱')
    password = wtf.PasswordField(u'密码', validators=[wtf.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise wtf.ValidationError('Duplicate username')


class CustomerForm(wtf.Form):
    address = wtf.TextField(u'地址', validators=[wtf.required()])
    phone = wtf.TextField(u'电话', validators=[wtf.required()])
    email = wtf.TextField(u'邮箱', validators=[wtf.required()])

    def validate_login(self, field):
        if not login.current_user.is_authenticated():
            raise wtf.ValidationError('Not login')

# Create menu links classes with reloaded accessible
class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return login.current_user.is_authenticated()


class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return not login.current_user.is_authenticated()


class UsernameMenuLink(AuthenticatedMenuLink):
    def __init__(self, url):
        self.url = url

    @property
    def name(self):
        return login.current_user.login
