# -*- coding: utf-8 -*-

from app import db

AUTO_MODEL = ['Credit', 'Customer', 'Delorder', 'Delorderinfo', 'Depart', 'Employee', 'Inaccount', 'Instockinform', 'Inventory', 'Lackorder', 'Msg', 'News', 'Orderinfo', 'Outaccount', 'Paybillaccount', 'Preorder', 'Preorderinfo', 'Product', 'Puraccount', 'Purorder', 'Reminder', 'Reminderinfo', 'Reorder', 'Sellaccount', 'Shoppingcart', 'Supplier', 'T_order']

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    ownMoney = db.Column(db.String(100))
    ownTime = db.Column(db.String(19))
    accumulateDebts = db.Column(db.String(100))
    beizhu = db.Column(db.String(100))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    name = db.Column(db.String(10))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(100))

class Delorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer)
    delPerson = db.Column(db.String(10))
    delTime = db.Column(db.String(19))
    driver = db.Column(db.String(10))
    driveTime = db.Column(db.String(19))
    delOrderStatus = db.Column(db.String(6))

class Delorderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delOrderId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    delNum = db.Column(db.Integer)

class Depart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departName = db.Column(db.String(10))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    empName = db.Column(db.String(10))
    empDepartId = db.Column(db.Integer)
    empSex = db.Column(db.String(2))
    empAddress = db.Column(db.String(60))
    empPhone = db.Column(db.String(11))

class Inaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer)
    inNum = db.Column(db.Integer)
    inTime = db.Column(db.String(19))
    inPerson = db.Column(db.String(10))

class Instockinform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    productNum = db.Column(db.Integer)
    time = db.Column(db.String(19))
    status = db.Column(db.String(6))

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer)
    number = db.Column(db.Integer)

class Lackorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderInfoId = db.Column(db.Integer)
    lackNum = db.Column(db.Integer)
    lackPerson = db.Column(db.String(10))
    lackTime = db.Column(db.String(19))
    lackOrderStatus = db.Column(db.String(6))

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.String(500))
    time = db.Column(db.String(19))

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(100))
    time = db.Column(db.String(19))

class Orderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    orderNum = db.Column(db.Integer)
    orderInfoStatus = db.Column(db.String(10))

class Outaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer)
    outNum = db.Column(db.Integer)
    outTime = db.Column(db.String(19))
    outPerson = db.Column(db.String(10))

class Paybillaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purOrderId = db.Column(db.Integer)
    supplierId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    purNum = db.Column(db.Integer)
    money = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))
    payBillStatus = db.Column(db.String(6))

class Preorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer)
    prePerson = db.Column(db.String(10))
    preOrderTime = db.Column(db.String(19))
    preOrderStatus = db.Column(db.String(10))

class Preorderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preOrderId = db.Column(db.Integer)
    orderInfoId = db.Column(db.Integer)
    preOrderNum = db.Column(db.Integer)
    preOrderPerson = db.Column(db.String(10))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(255))
    originalId = db.Column(db.String(255))
    salePrice = db.Column(db.String(20))
    buyPrice = db.Column(db.String(20))
    description = db.Column(db.String(500))
    type = db.Column(db.String(10))

class Puraccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purOrderId = db.Column(db.Integer)
    supplierId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    purNum = db.Column(db.Integer)
    money = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))

class Purorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    purNum = db.Column(db.Integer)
    purPerson = db.Column(db.String(10))
    purTime = db.Column(db.String(19))
    getTime = db.Column(db.String(19))
    purOrderStatus = db.Column(db.String(6))

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delOrderId = db.Column(db.Integer)
    fare = db.Column(db.String(100))
    totalMoney = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))
    recMoneyTime = db.Column(db.String(19))
    reminderStatus = db.Column(db.String(6))

class Reminderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reminderId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    delNum = db.Column(db.Integer)
    price = db.Column(db.String(50))
    money = db.Column(db.String(100))

class Reorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer)
    reorderNum = db.Column(db.Integer)
    reorderLevel = db.Column(db.String(10))
    reorderPerson = db.Column(db.String(10))
    reorderTime = db.Column(db.String(19))
    reorderStatus = db.Column(db.String(6))

class Sellaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    reminderId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    sellNum = db.Column(db.Integer)
    money = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))

class Shoppingcart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    orderNum = db.Column(db.Integer)
    money = db.Column(db.String(500))
    flag = db.Column(db.Integer)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierName = db.Column(db.String(255))
    supplierAdd = db.Column(db.String(255))
    supplierPhone = db.Column(db.String(11))

class T_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    receiver = db.Column(db.String(20))
    receiverAdd = db.Column(db.String(255))
    receiverPhone = db.Column(db.String(11))
    orderTime = db.Column(db.String(19))
    orderStatus = db.Column(db.String(6))
    unitedOrderId = db.Column(db.String(23))
    totalMoney = db.Column(db.String(10))
    type = db.Column(db.String(10))