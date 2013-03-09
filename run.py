# -*- coding: utf-8 -*-

from time import gmtime, strftime

from flask import url_for, redirect, render_template, request, flash
from flask.ext import login, admin
from app import app, db

import auto_model

from auto_model import *
from model import User
from helper import LoginForm, RegistrationForm, CustomerForm, \
    UsernameMenuLink, AuthenticatedMenuLink, NotAuthenticatedMenuLink
from view import CartView, MyModelView, RoleView


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
    return redirect(url_for('admin.index'))


@app.route('/checkout/', methods=['GET', 'POST'])
def checkout():
    userId = login.current_user.id
    customer = db.session.query(Customer).filter_by(userId=userId).first()
    if not customer:
        return redirect(url_for('reg_customer_view'))
    
    form = request.form
    currency = form['currency']
    shipping = form['shipping']
    tax = form['tax']
    taxRate = form['taxRate']
    itemCount = int(form['itemCount'])

    items = []
    for i in range(itemCount):
        item = {}
        item['id'] = int(form['item_name_%s' % (i+1)].split('_')[1])
        item['count'] = int(form['item_quantity_%s' % (i+1)])
        item['price'] = float(form['item_price_%s' % (i+1)])
        items.append(item)
    
    orderId = handle_order(items, customer)
    if orderId:
        flash(u'订单提交成功! 订单号: %s' % orderId)
    else:
        flash(u'订单提交失败，请重试!')
    return redirect(url_for('index'))


def handle_order(items, customer):
    receiver = customer.accountName
    receiverAdd = customer.address
    receiverPhone = customer.phone
    orderStatus = 'ready'
    orderTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    totalMoney = 0.0
    for item in items:
        totalMoney += item['count'] * item['price']
    torder = Torder(customer=customer, receiver=receiver, receiverAdd=receiverAdd,
                    receiverPhone=receiverPhone, orderStatus=orderStatus, 
                    orderTime=orderTime, totalMoney=totalMoney, type=0)
    db.session.add(torder)

    preorder = Preorder(torder=torder, prePerson='xiaoshou', preOrderTime=orderTime, preOrderStatus='ready')
    db.session.add(preorder)

    is_lack = False
    for item in items:
        i_id = item['id']
        count = item['count']
        inventory = Inventory.query.filter_by(id=i_id).first()
        if inventory:
            inventory_num = inventory.number
            if count > inventory_num:
                is_lack = True
                s = 'lack'
            else:
                s = 'ready'
            orderinfo = Orderinfo(torder=torder, productId=item['id'], orderNum=item['count'], orderInfoStatus=s)
            if s == 'lack':
                if not handle_lack_order(item, orderinfo, count-inventory_num, orderTime):
                    return False
            elif s == 'ready':
                if not handle_pre_order(item, orderinfo, preorder, count, orderTime):
                    return False
        else:
            return False
        db.session.add(orderinfo)
    if is_lack:
        torder.orderStatus = 'lack'
    db.session.commit()
    db.session.refresh(torder)
    orderId = torder.id
    return orderId


def handle_pre_order(item, orderinfo, preorder, count, orderTime):
    preorderinfo = Preorderinfo(preorder=preorder, orderinfo=orderinfo, preOrderNum=count, preOrderPerson='xiaoshou')
    db.session.add(preorderinfo)
    return True

def handle_lack_order(item, orderinfo, num, orderTime):
    lackorder = Lackorder(orderinfo=orderinfo, lackNum=num, lackPerson='xiaoshou', lackTime=orderTime, lackOrderStatus='lack')
    db.session.add(lackorder)
    return True


@app.route('/reg_customer/', methods=('GET', 'POST'))
def reg_customer_view():
    form = CustomerForm(request.form)
    if form.validate_on_submit():
        customer = Customer()

        form.populate_obj(customer)
        customer.accountName = login.current_user.login
        customer.userId = login.current_user.id
        customer.email = login.current_user.email

        db.session.add(customer)
        db.session.commit()
        flash(u'注册顾客信息成功，请重新提交订单!')
        return redirect(url_for('index'))

    return render_template('form.html', form=form)


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
    admin = admin.Admin(app, 'AMC')

    # Add views
    for m in auto_model.__all__:
        m = getattr(auto_model, m)
        c = m.category()
        n = m.name()
        desc = m.desc()
        if c != 'Other':
            if desc != 'None':
                admin.add_view(MyModelView(m, db.session, name=n, category=c, desc=desc))
            else:
                admin.add_view(MyModelView(m, db.session, name=n, category=c))

    admin.add_view(RoleView(User, db.session, name=u'用户'))
    admin.add_view(CartView(name=u'购物车'))

    # Add username link
    admin.add_link(UsernameMenuLink(url='#'))

    # Add register link by endpoint
    admin.add_link(NotAuthenticatedMenuLink(name=u'注册',
                                            endpoint='register_view'))

    # Add login link by endpoint
    admin.add_link(NotAuthenticatedMenuLink(name=u'登录',
                                            endpoint='login_view'))

    # Add logout link by endpoint
    admin.add_link(AuthenticatedMenuLink(name=u'登出',
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
