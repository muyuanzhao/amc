# -*- coding: utf-8 -*-

import codecs

from flask.ext import login
from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib import sqlamodel
from wtforms.fields import SelectField
from auto_model import Preorder

CUSTOMER_ACCESSIBLE_MODELS = (Preorder,)


class CartView(BaseView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

    @expose('/')
    def index(self):
        return self.render('cart.html')


# Create customized model view class
class MyModelView(sqlamodel.ModelView):
    column_labels = {}
    with codecs.open(r'i18n/zh_cn.txt', 'r', encoding='utf-8') as tf:
        for line in tf.readlines():
            db_name, view_name = line.strip().split()
            column_labels[db_name] = view_name

    def __init__(self, model, session,
                 name=None, category=None, endpoint=None, url=None, desc=None):
        self.desc = desc
        super(MyModelView, self).__init__(model, session,
                                          name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self):
        # add user access level
        return login.current_user.is_authenticated() \
            and (login.current_user.role == '1' or self.model in CUSTOMER_ACCESSIBLE_MODELS)


class RoleView(MyModelView):
    form_overrides = dict(role=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        role=dict(
            choices=[('0', u'顾客'), ('1', u'管理员'), ('2', u'销售'), ('3', u'财务'), ('4', u'采购'), ('5', u'库存'), ('6', u'发货')]
        ))
