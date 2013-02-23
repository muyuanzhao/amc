# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Create application
app = Flask('amc')

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@localhost/amc?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
