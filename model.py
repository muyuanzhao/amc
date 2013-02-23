# -*- coding: utf-8 -*-

from app import db

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

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    ownMoney = db.Column(db.String(100))
    ownTime = db.Column(db.String(19))
    accumulateDebts = db.Column(db.String(100))
    beizhu = db.Column(db.String(100))

