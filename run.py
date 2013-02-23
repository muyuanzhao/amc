# -*- coding: utf-8 -*-

from flask import url_for, redirect, render_template, request
from flask.ext import login, admin
from model import User
from view import MyAdminIndexView, IndexView
from app import app, db
from helper import LoginForm, RegistrationForm


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
    return render_template('index.html', user=login.current_user)


@app.route('/login/', methods=('GET', 'POST'))
def login_view():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = form.get_user()
        login.login_user(user)
        return redirect(url_for('index'))

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
        return redirect(url_for('index'))

    return render_template('form.html', form=form)


@app.route('/logout/')
def logout_view():
    login.logout_user()
    return redirect(url_for('index'))
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
