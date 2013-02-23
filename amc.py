# -*- coding: utf-8 -*-

from flask import Flask, url_for, redirect, render_template, request
from flask.ext import login, admin, wtf
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin, BaseView, expose
from model import User

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@localhost/amc?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Create customized index view class
class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


class IndexView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.setup_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


if __name__ == '__main__':
    # Initialize flask-login
    init_login()

    # Create admin
    admin = admin.Admin(app, 'AMC', index_view=MyAdminIndexView())

    # Add views
    admin.add_view(IndexView(name=u'订单处理'))

    # Create DB
    db.create_all()

    # Start app
    app.debug = True
    app.run()
