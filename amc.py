# -*- coding: utf-8 -*-

from flask import url_for, redirect, render_template, request
from flask.ext import login, admin
from flask.ext.admin import Admin, BaseView, expose
from model import User
from view import MyAdminIndexView, IndexView
from app import app, db


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
