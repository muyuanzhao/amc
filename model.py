# -*- coding: utf-8 -*-

from flask.ext import login
from flask.ext.admin.contrib import sqlamodel
from app import db


# Create customized model view class
class MyModelView(sqlamodel.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username
