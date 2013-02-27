# -*- coding: utf-8 -*-

from flask import url_for, redirect, render_template, request
from flask.ext import login, admin
from app import app, db

import auto_model

from model import User
from helper import LoginForm, RegistrationForm, \
    UsernameMenuLink, AuthenticatedMenuLink, NotAuthenticatedMenuLink
from view import MyModelView, RoleView


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.setup_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


@app.route('/')
def index():
    return render_template('shop.html')


@app.route('/login/', methods=('GET', 'POST'))
def login_view():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = form.get_user()
        login.login_user(user)
        return redirect(url_for('admin.index'))

    return render_template('form.html', form=form)


@app.route('/register/', methods=('GET', 'POST'))
def register_view():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User()

        form.populate_obj(user)

        db.session.add(user)
        db.session.commit()

        login.login_user(user)
        return redirect(url_for('admin.index'))

    return render_template('form.html', form=form)


@app.route('/logout/')
def logout_view():
    login.logout_user()
    return redirect(url_for('admin.index'))


if __name__ == '__main__':
    # Initialize flask-login
    init_login()

    # Create admin
    admin = admin.Admin(app, 'AMC')

    # Add views
    for m in auto_model.__all__:
        m = getattr(auto_model, m)
        admin.add_view(MyModelView(m, db.session, category=m.category()))

    admin.add_view(RoleView(User, db.session))

    # Add username link
    admin.add_link(UsernameMenuLink(url='#'))

    # Add register link by endpoint
    admin.add_link(NotAuthenticatedMenuLink(name='Register',
                                            endpoint='register_view'))

    # Add login link by endpoint
    admin.add_link(NotAuthenticatedMenuLink(name='Login',
                                            endpoint='login_view'))

    # Add logout link by endpoint
    admin.add_link(AuthenticatedMenuLink(name='Logout',
                                         endpoint='logout_view'))
    # Create DB
    db.create_all()

    # Add admin user
    if User.query.filter_by(login='admin').first() is None:
        admin = User('admin', 'admin@amc.com', 'admin', '1')
        db.session.add(admin)
        db.session.commit()

    # Start app
    app.debug = True
    app.run()
