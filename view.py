# -*- coding: utf-8 -*-

from flask.ext import login
from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib import sqlamodel
from wtforms.fields import SelectField
from auto_model import Preorder

CUSTOMER_ACCESSIBLE_MODELS = (Preorder,)


class IndexView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


# Create customized model view class
class MyModelView(sqlamodel.ModelView):
    def is_accessible(self):
        # add user access level
        return login.current_user.is_authenticated() \
            and (login.current_user.role == '1' or self.model in CUSTOMER_ACCESSIBLE_MODELS)


class RoleView(MyModelView):
    form_overrides = dict(role=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        role=dict(
            choices=[('0', 'customer'), ('1', 'employee')]
        ))
