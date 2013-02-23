# -*- coding: utf-8 -*-

from flask.ext import login, admin
from flask.ext.admin import BaseView, expose


# Create customized index view class
class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


class IndexView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')
