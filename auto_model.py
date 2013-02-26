# -*- coding: utf-8 -*-

from app import db

__all__ = ['Credit', 'Customer', 'Delorder', 'Delorderinfo', 'Depart', 'Employee', 'Inaccount', 'Instockinform', 'Inventory', 'Lackorder', 'Msg', 'News', 'Orderinfo', 'Outaccount', 'Paybillaccount', 'Preorder', 'Preorderinfo', 'Product', 'Puraccount', 'Purorder', 'Reminder', 'Reminderinfo', 'Reorder', 'Sellaccount', 'Shoppingcart', 'Supplier', 'T_order']


class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==Credit.customerId')
    ownMoney = db.Column(db.String(100))
    ownTime = db.Column(db.String(19))
    accumulateDebts = db.Column(db.String(100))
    beizhu = db.Column(db.String(100))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Finance'



class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', primaryjoin='User.id==Customer.userId')
    name = db.Column(db.String(10))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(100))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'People'



class Delorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('T_order.id'))
    T_order = db.relationship('T_order', primaryjoin='T_order.id==Delorder.orderId')
    delPerson = db.Column(db.String(10))
    delTime = db.Column(db.String(19))
    driver = db.Column(db.String(10))
    driveTime = db.Column(db.String(19))
    delOrderStatus = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Order'



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
    def _category(cls):
        return 'Order'



class Depart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departName = db.Column(db.String(10))

    def __repr__(self):
        return self.departName


    @classmethod
    def _category(cls):
        return 'People'



class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', primaryjoin='User.id==Employee.userId')
    empName = db.Column(db.String(10))
    empDepartId = db.Column(db.Integer, db.ForeignKey('depart.id'))
    depart = db.relationship('Depart', primaryjoin='Depart.id==Employee.empDepartId')
    empSex = db.Column(db.String(2))
    empAddress = db.Column(db.String(60))
    empPhone = db.Column(db.String(11))

    def __repr__(self):
        return self.empName


    @classmethod
    def _category(cls):
        return 'People'



class Inaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Inaccount.productId')
    inNum = db.Column(db.Integer)
    inTime = db.Column(db.String(19))
    inPerson = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Finance'



class Instockinform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierId = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    supplier = db.relationship('Supplier', primaryjoin='Supplier.id==Instockinform.supplierId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Instockinform.productId')
    productNum = db.Column(db.Integer)
    time = db.Column(db.String(19))
    status = db.Column(db.String(6))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Inventory'



class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Inventory.productId')
    number = db.Column(db.Integer)

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Inventory'



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
    def _category(cls):
        return 'Order'



class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.String(500))
    time = db.Column(db.String(19))

    def __repr__(self):
        return self.userName


    @classmethod
    def _category(cls):
        return 'Notice'



class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(100))
    time = db.Column(db.String(19))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Notice'



class Orderinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('T_order.id'))
    T_order = db.relationship('T_order', primaryjoin='T_order.id==Orderinfo.orderId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Orderinfo.productId')
    orderNum = db.Column(db.Integer)
    orderInfoStatus = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Order'



class Outaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Outaccount.productId')
    outNum = db.Column(db.Integer)
    outTime = db.Column(db.String(19))
    outPerson = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Finance'



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
    def _category(cls):
        return 'Finance'



class Preorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('T_order.id'))
    T_order = db.relationship('T_order', primaryjoin='T_order.id==Preorder.orderId')
    prePerson = db.Column(db.String(10))
    preOrderTime = db.Column(db.String(19))
    preOrderStatus = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Order'



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
    def _category(cls):
        return 'Order'



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(255))
    originalId = db.Column(db.String(255))
    salePrice = db.Column(db.String(20))
    buyPrice = db.Column(db.String(20))
    description = db.Column(db.String(500))
    type = db.Column(db.String(10))

    def __repr__(self):
        return self.productName


    @classmethod
    def _category(cls):
        return 'Product'



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
    def _category(cls):
        return 'Finance'



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
    def _category(cls):
        return 'Order'



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
    def _category(cls):
        return 'Notice'



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
    def _category(cls):
        return 'Notice'



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
    def _category(cls):
        return 'Order'



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
    def _category(cls):
        return 'Finance'



class Shoppingcart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==Shoppingcart.customerId')
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', primaryjoin='Product.id==Shoppingcart.productId')
    orderNum = db.Column(db.Integer)
    money = db.Column(db.String(500))
    flag = db.Column(db.Integer)

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'EC'



class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierName = db.Column(db.String(255))
    supplierAdd = db.Column(db.String(255))
    supplierPhone = db.Column(db.String(11))

    def __repr__(self):
        return self.supplierName


    @classmethod
    def _category(cls):
        return 'Supplier'



class T_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', primaryjoin='Customer.id==T_order.customerId')
    receiver = db.Column(db.String(20))
    receiverAdd = db.Column(db.String(255))
    receiverPhone = db.Column(db.String(11))
    orderTime = db.Column(db.String(19))
    orderStatus = db.Column(db.String(6))
    unitedOrderId = db.Column(db.String(23))
    totalMoney = db.Column(db.String(10))
    type = db.Column(db.String(10))

    def __repr__(self):
        return str(self.id)


    @classmethod
    def _category(cls):
        return 'Order'
