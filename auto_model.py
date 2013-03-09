# -*- coding: utf-8 -*-

from model import User
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

    @classmethod
    def name(cls):
        return u'客户信息'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1', '2']


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

    @classmethod
    def name(cls):
        return u'客户信用'

    @classmethod
    def desc(cls):
        return u'在填写备货单时，要查阅顾客档案，将顾客的详细收货地址、收货人、顾客的信用及其它有关内容镇人。在收到新顾客的订单后，由负责处理此订单的人员将该顾客的详细情况记载在顾客档案中。会计室要及时将顾客的失信情况填写失信通知单（附表8）通知销售办公室，由销售办公室记录在顾客档案上。'

    @classmethod
    def roles(cls):
        return ['1', '2']


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

    @classmethod
    def name(cls):
        return u'员工信息'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1']


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplierName = db.Column(db.String(255))
    supplierAdd = db.Column(db.String(255))
    supplierPhone = db.Column(db.String(11))

    def __repr__(self):
        return self.supplierName

    @classmethod
    def category(cls):
        return u'采购部'

    @classmethod
    def name(cls):
        return u'供货商信息'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1', '4']


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

    @classmethod
    def name(cls):
        return u'库存信息'

    @classmethod
    def desc(cls):
        return u'仓库根据备货单备货，填写出、人库台帐，修改库存。当某备货单上的项目全部处理完后，交打字员小吴打印一式四份的发货单（附表4），一份留底，三份连同货物交包装、发货组。在备货的同时，要检查每种配件的库存水平，如已达到“再订货水平”、“危险水平”或“缺货水平”，除在货物架上放置有关卡片外，要填写再订货通知单（附表5）交采购办公室。当收到进货通知单和新购入的配件后，要登帐和上架。所有货物的运输都由搬运工负责。'

    @classmethod
    def roles(cls):
        return ['1', '5']


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
        return u'库存部'

    @classmethod
    def name(cls):
        return u'产品信息'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1', '4', '5']


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

    @classmethod
    def name(cls):
        return u'删除订单'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1']


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

    @classmethod
    def name(cls):
        return u'Other'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1']


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

    @classmethod
    def name(cls):
        return u'缺货单'

    @classmethod
    def desc(cls):
        return u'对于可供货项目和部分可供货的项目，按订单号分别开备货单（附表3）交仓库，同时修改库存记录。对于完全缺货的订单另行保管；对于部分缺货的订单先供应一部分，将尚缺的数量用订单缺件表（附表1）记载下来。'

    @classmethod
    def roles(cls):
        return ['1', '2']


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
        return u'订单'

    @classmethod
    def name(cls):
        return u'订单详情'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1', '2']


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

    @classmethod
    def name(cls):
        return u'备货单'

    @classmethod
    def desc(cls):
        return u'在填写备货单时，要查阅顾客档案，将顾客的详细收货地址、收货人、顾客的信用及其它有关内容镇人。在收到新顾客的订单后，由负责处理此订单的人员将该顾客的详细情况记载在顾客档案中。备货单上要有订货单位的自编号和本公司接收订单的统一编号。每天11：00和16：00由办事员小彭统一将备货单送到仓库。'

    @classmethod
    def roles(cls):
        return ['1', '2']


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
        return u'订单'

    @classmethod
    def name(cls):
        return u'备货单详情'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1', '2']


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

    @classmethod
    def name(cls):
        return u'付款账户'

    @classmethod
    def desc(cls):
        return u'在收到供货厂家的催款单后，记应付帐、付款。待发票寄来后，还要转采购业务帐。'

    @classmethod
    def roles(cls):
        return ['1', '3']


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

    @classmethod
    def name(cls):
        return u'采购账户'

    @classmethod
    def desc(cls):
        return u'通常，本公司的采购部是采用订单订货，当收到厂家发来的汽车配件和催款单后，根据订单留底进行货、款核对，然后，催款单交会计室，验收后的配件交库房，另外，填写进货通知单（附表9）一式两份，一份随同配件送库房，一份送销售办公室。'

    @classmethod
    def roles(cls):
        return ['1', '3']


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

    @classmethod
    def name(cls):
        return u'销售账户'

    @classmethod
    def desc(cls):
        return u'会计室对发货单（3）进行计价，记应收帐，开催款单（附表6），并将催款单寄给顾客 当收到顾客货款（支票、汇款单或银行转帐通知单）后，转销售业务帐，开发票（附表7）寄给顾客。'

    @classmethod
    def roles(cls):
        return ['1', '3']


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

    @classmethod
    def name(cls):
        return u'采购订单'

    @classmethod
    def desc(cls):
        return u'采购办公室订货主要是根据供货厂家的产品目录和销售办公室提供的缺货通知单及仓库提供的再订货通知单，有时，也由推销员提供一些需要采购的新品种。通常，本公司的采购部是采用订单订货，当收到厂家发来的汽车配件和催款单后，根据订单留底进行货、款核对，然后，催款单交会计室，验收后的配件交库房，另外，填写进货通知单（附表9）一式两份，一份随同配件送库房，一份送销售办公室。'

    @classmethod
    def roles(cls):
        return ['1', '4']


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

    @classmethod
    def name(cls):
        return u'订单提醒'

    @classmethod
    def desc(cls):
        return u'当收到进货通知单后，赵清玉和小杨先修改库存记录，再进行缺货处理。为了使缺货证件及时得到补充，必须尽早填写缺货通知单（附表2）送采购部门。'

    @classmethod
    def roles(cls):
        return ['1']


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

    @classmethod
    def name(cls):
        return u'Other'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1']


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

    @classmethod
    def name(cls):
        return u'再订货订单'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1', '2']


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

    @classmethod
    def name(cls):
        return u'订单信息'

    @classmethod
    def desc(cls):
        return u'销售办公室的李英专门负责订单校验，若遇有填写不清楚或错误的订单退回给顾客。然后，由张小辉等三人根据订单上的配件项目，逐项查阅库存记录，将缺货项目和可供货项目分开。'

    @classmethod
    def roles(cls):
        return ['1', '2']


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

    @classmethod
    def name(cls):
        return u'Other'

    @classmethod
    def desc(cls):
        return u'None'

    @classmethod
    def roles(cls):
        return ['1']