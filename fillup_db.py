# -*- coding: utf-8 -*-

from app import db
from auto_model import Product, Inventory

for i in xrange(10):
    product = Product(productName=u'product_' + str(i),
                      salePrice=str(100.99 + 10 * i),
                      buyPrice=str(60.99 + 10 * i),
                      description='product',
                      type='0')
    inventory = Inventory(product=product,
                          number=i * 10)
    db.session.add(product)
    db.session.add(inventory)

db.session.commit()
