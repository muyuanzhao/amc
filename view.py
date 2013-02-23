# -*- coding: utf-8 -*-

from flask.ext import login, admin
from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib import sqlamodel


# Create customized index view class
class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


class IndexView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

# Create customized model view class
class MyModelView(sqlamodel.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()
