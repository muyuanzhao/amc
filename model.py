# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))
    role = db.Column(db.String(64))

    def __init__(self, login=None, email=None, password=None, role=None):
        self.login = login
        self.email = email
        self.password = password
        self.role = role

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
