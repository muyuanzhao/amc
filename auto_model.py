# -*- coding: utf-8 -*-

from app import db

__all__ = ['Customer', 'Credit', 'Employee', 'Supplier', 'Inventory', 'Product', 'Delorder', 'Delorderinfo', 'Lackorder', 'Orderinfo', 'Preorder', 'Preorderinfo', 'Paybillaccount', 'Puraccount', 'Sellaccount', 'Purorder', 'Reminder', 'Reminderinfo', 'Reorder', 'Torder', 'Shoppingcart']


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', primaryjoin='User.id==Customer.userId')
    accountName = db.Column(db.String(10))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(100))

    def __repr__(self):
        return self.accountName

    @classmethod
    def category(cls):
        return u'销售部'


class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==Credit.customerId')
    ownMoney = db.Column(db.String(100))
    ownTime = db.Column(db.String(19))
    accumulateDebt = db.Column(db.String(100))
    remark = db.Column(db.String(100))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'销售部'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', primaryjoin='User.id==Employee.userId')
    empName = db.Column(db.String(10))
    sex = db.Column(db.String(2))
    address = db.Column(db.String(60))
    phone = db.Column(db.String(11))

    def __repr__(self):
        return self.empName

    @classmethod
    def category(cls):
        return u'员工'


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierName = db.Column(db.String(255))
    supplierAdd = db.Column(db.String(255))
    supplierPhone = db.Column(db.String(11))

    def __repr__(self):
        return self.supplierName

    @classmethod
    def category(cls):
        return u'供货商'


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Inventory.productId')
    number = db.Column(db.Integer)

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'库存部'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(255))
    salePrice = db.Column(db.String(20))
    buyPrice = db.Column(db.String(20))
    description = db.Column(db.String(500))
    type = db.Column(db.String(10))

    def __repr__(self):
        return self.productName

    @classmethod
    def category(cls):
        return u'产品'


class Delorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('torder.id'))
    torder = db.relationship('Torder', primaryjoin='Torder.id==Delorder.orderId')
    delPerson = db.Column(db.String(10))
    delTime = db.Column(db.String(19))
    driver = db.Column(db.String(10))
    driveTime = db.Column(db.String(19))
    delOrderStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'订单'


class Delorderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delOrderId = db.Column(db.Integer, db.ForeignKey('delorder.id'))
    delorder = db.relationship('Delorder', primaryjoin='Delorder.id==Delorderinfo.delOrderId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Delorderinfo.productId')
    delNum = db.Column(db.Integer)

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'Other'


class Lackorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderInfoId = db.Column(db.Integer, db.ForeignKey('orderinfo.id'))
    orderinfo = db.relationship('Orderinfo', primaryjoin='Orderinfo.id==Lackorder.orderInfoId')
    lackNum = db.Column(db.Integer)
    lackPerson = db.Column(db.String(10))
    lackTime = db.Column(db.String(19))
    lackOrderStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'订单'


class Orderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('torder.id'))
    torder = db.relationship('Torder', primaryjoin='Torder.id==Orderinfo.orderId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Orderinfo.productId')
    orderNum = db.Column(db.Integer)
    orderInfoStatus = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'Other'


class Preorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('torder.id'))
    torder = db.relationship('Torder', primaryjoin='Torder.id==Preorder.orderId')
    prePerson = db.Column(db.String(10))
    preOrderTime = db.Column(db.String(19))
    preOrderStatus = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'订单'


class Preorderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preOrderId = db.Column(db.Integer, db.ForeignKey('preorder.id'))
    preorder = db.relationship('Preorder', primaryjoin='Preorder.id==Preorderinfo.preOrderId')
    orderInfoId = db.Column(db.Integer, db.ForeignKey('orderinfo.id'))
    orderinfo = db.relationship('Orderinfo', primaryjoin='Orderinfo.id==Preorderinfo.orderInfoId')
    preOrderNum = db.Column(db.Integer)
    preOrderPerson = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'Other'


class Paybillaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purOrderId = db.Column(db.Integer, db.ForeignKey('purorder.id'))
    purorder = db.relationship('Purorder', primaryjoin='Purorder.id==Paybillaccount.purOrderId')
    supplierId = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    supplier = db.relationship('Supplier', primaryjoin='Supplier.id==Paybillaccount.supplierId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Paybillaccount.productId')
    purNum = db.Column(db.Integer)
    money = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))
    payBillStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'财务部'


class Puraccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purOrderId = db.Column(db.Integer, db.ForeignKey('purorder.id'))
    purorder = db.relationship('Purorder', primaryjoin='Purorder.id==Puraccount.purOrderId')
    supplierId = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    supplier = db.relationship('Supplier', primaryjoin='Supplier.id==Puraccount.supplierId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Puraccount.productId')
    purNum = db.Column(db.Integer)
    money = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'财务部'


class Sellaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==Sellaccount.customerId')
    reminderId = db.Column(db.Integer, db.ForeignKey('reminder.id'))
    reminder = db.relationship('Reminder', primaryjoin='Reminder.id==Sellaccount.reminderId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Sellaccount.productId')
    sellNum = db.Column(db.Integer)
    money = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'财务部'


class Purorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierId = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    supplier = db.relationship('Supplier', primaryjoin='Supplier.id==Purorder.supplierId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Purorder.productId')
    purNum = db.Column(db.Integer)
    purPerson = db.Column(db.String(10))
    purTime = db.Column(db.String(19))
    getTime = db.Column(db.String(19))
    purOrderStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'订单'


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delOrderId = db.Column(db.Integer, db.ForeignKey('delorder.id'))
    delorder = db.relationship('Delorder', primaryjoin='Delorder.id==Reminder.delOrderId')
    fare = db.Column(db.String(100))
    totalMoney = db.Column(db.String(100))
    accountPerson = db.Column(db.String(10))
    accountTime = db.Column(db.String(19))
    recMoneyTime = db.Column(db.String(19))
    reminderStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'提醒'


class Reminderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reminderId = db.Column(db.Integer, db.ForeignKey('reminder.id'))
    reminder = db.relationship('Reminder', primaryjoin='Reminder.id==Reminderinfo.reminderId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Reminderinfo.productId')
    delNum = db.Column(db.Integer)
    price = db.Column(db.String(50))
    money = db.Column(db.String(100))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'Other'


class Reorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Reorder.productId')
    reorderNum = db.Column(db.Integer)
    reorderLevel = db.Column(db.String(10))
    reorderPerson = db.Column(db.String(10))
    reorderTime = db.Column(db.String(19))
    reorderStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'订单'


class Torder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==Torder.customerId')
    receiver = db.Column(db.String(20))
    receiverAdd = db.Column(db.String(255))
    receiverPhone = db.Column(db.String(11))
    orderTime = db.Column(db.String(19))
    orderStatus = db.Column(db.String(6))
    totalMoney = db.Column(db.String(10))
    type = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'订单'


class Shoppingcart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==Shoppingcart.customerId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Shoppingcart.productId')
    orderNum = db.Column(db.Integer)
    money = db.Column(db.String(500))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def category(cls):
        return u'Other'