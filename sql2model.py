#-*- coding: utf-8 -*-
'''
A simple script for transforming sql to python model class, it is just hard coding
not involved with SQL grammar structure.Our sql file doesn't contain FK definition,
so we identify it by column attribute name, like xxxId.
'''

import re
import codecs


COMMENT_LINE = '--'
COMMENT_PAIRS = {'START': '/*',
                 'END': '*/'}

OPS = ('SET',
       'DROP',
       'CREATE',
       )

category_dict = {'Credit': u'销售部', 'Customer': u'销售部', 'Delorder': u'订单', 'Delorderinfo': 'Other', 'Employee': u'员工', 'Inventory': u'库存部', 'Lackorder': u'订单', 'Orderinfo': 'Other',  'Paybillaccount': u'财务部', 'Preorder': u'订单', 'Preorderinfo': 'Other', 'Product': u'产品', 'Puraccount': u'财务部', 'Purorder': u'订单', 'Reminder': u'提醒', 'Reminderinfo': 'Other', 'Reorder': u'订单', 'Sellaccount': u'财务部', 'Shoppingcart': 'Other', 'Supplier': u'供货商', 'Torder': u'订单'}

name_dict = {'Credit': u'客户信用', 'Customer': u'客户信息', 'Delorder': u'删除订单', 'Delorderinfo': 'Other', 'Employee': u'员工信息', 'Inventory': u'库存信息', 'Lackorder': u'缺货单', 'Orderinfo': 'Other',  'Paybillaccount': u'付款账户', 'Preorder': u'备货单', 'Preorderinfo': 'Other', 'Product': u'产品信息', 'Puraccount': u'采购账户', 'Purorder': u'采购订单', 'Reminder': u'订单提醒', 'Reminderinfo': 'Other', 'Reorder': u'再订货订单', 'Sellaccount': u'销售账户', 'Shoppingcart': 'Other', 'Supplier': u'供货商信息', 'Torder': u'订单信息'}

desc_dict = {'Credit': u'在填写备货单时，要查阅顾客档案，将顾客的详细收货地址、收货人、顾客的信用及其它有关内容镇人。在收到新顾客的订单后，由负责处理此订单的人员将该顾客的详细情况记载在顾客档案中。会计室要及时将顾客的失信情况填写失信通知单（附表8）通知销售办公室，由销售办公室记录在顾客档案上。',
             'Torder': u'销售办公室的李英专门负责订单校验，若遇有填写不清楚或错误的订单退回给顾客。然后，由张小辉等三人根据订单上的配件项目，逐项查阅库存记录，将缺货项目和可供货项目分开。',
             'Preorder': u'在填写备货单时，要查阅顾客档案，将顾客的详细收货地址、收货人、顾客的信用及其它有关内容镇人。在收到新顾客的订单后，由负责处理此订单的人员将该顾客的详细情况记载在顾客档案中。备货单上要有订货单位的自编号和本公司接收订单的统一编号。每天11：00和16：00由办事员小彭统一将备货单送到仓库。',
             'Lackorder': u'对于可供货项目和部分可供货的项目，按订单号分别开备货单（附表3）交仓库，同时修改库存记录。对于完全缺货的订单另行保管；对于部分缺货的订单先供应一部分，将尚缺的数量用订单缺件表（附表1）记载下来。',
             'Purorder': u'采购办公室订货主要是根据供货厂家的产品目录和销售办公室提供的缺货通知单及仓库提供的再订货通知单，有时，也由推销员提供一些需要采购的新品种。通常，本公司的采购部是采用订单订货，当收到厂家发来的汽车配件和催款单后，根据订单留底进行货、款核对，然后，催款单交会计室，验收后的配件交库房，另外，填写进货通知单（附表9）一式两份，一份随同配件送库房，一份送销售办公室。',
             'Reminder': u'当收到进货通知单后，赵清玉和小杨先修改库存记录，再进行缺货处理。为了使缺货证件及时得到补充，必须尽早填写缺货通知单（附表2）送采购部门。',
             'Inventory': u'仓库根据备货单备货，填写出、人库台帐，修改库存。当某备货单上的项目全部处理完后，交打字员小吴打印一式四份的发货单（附表4），一份留底，三份连同货物交包装、发货组。在备货的同时，要检查每种配件的库存水平，如已达到“再订货水平”、“危险水平”或“缺货水平”，除在货物架上放置有关卡片外，要填写再订货通知单（附表5）交采购办公室。当收到进货通知单和新购入的配件后，要登帐和上架。所有货物的运输都由搬运工负责。',
             'Sellaccount': u'会计室对发货单（3）进行计价，记应收帐，开催款单（附表6），并将催款单寄给顾客 当收到顾客货款（支票、汇款单或银行转帐通知单）后，转销售业务帐，开发票（附表7）寄给顾客。',
             'Paybillaccount': u'在收到供货厂家的催款单后，记应付帐、付款。待发票寄来后，还要转采购业务帐。',
             'Puraccount': u'通常，本公司的采购部是采用订单订货，当收到厂家发来的汽车配件和催款单后，根据订单留底进行货、款核对，然后，催款单交会计室，验收后的配件交库房，另外，填写进货通知单（附表9）一式两份，一份随同配件送库房，一份送销售办公室。'
             }

sql_file = codecs.open('amc.sql', 'r', encoding='utf-8')
sql_lines = sql_file.readlines()
sql_file.close()


def op_handler(op, data):
    if op == 'create':
        return create_sql(data)
    else:
        return None, None


def type_transform(t):
    if t.startswith('int'):
        return 'db.Integer'
    elif t.startswith('varchar') or t.startswith('char'):
        m = re.search(r'(\d+)', t)
        assert m, 'No arg in %s --' % t
        return 'db.String(%s)' % int(m.group(1))
    elif t.startswith('text'):
        return 'db.String(100)'
    else:
        print 'What type? -- %s' % t
        return 'db.String(100)'


def create_sql(sql):
    #first line is like CREATE TABLE XXX (
    class_name = sql[0].split()[2][1:-1].capitalize()
    if class_name == 'User':
        return None, None

    #scan for PK
    attrs = []
    pk = None
    representation = None
    category = category_dict.get(class_name, 'Other')
    name = name_dict.get(class_name, 'Other')
    desc = desc_dict.get(class_name, 'None')
    for line in sql[1:-1]:
        if line.startswith('PRIMARY KEY'):
            pk = line.split()[2][2:-2]
            break
    assert pk, 'No PK'

    #others until PK
    for line in sql[1:-2]:
        tokens = line.split()
        attr_name = tokens[0][1:-1]
        attr_type = type_transform(tokens[1])
        assert attr_type, line
        if 'Name' in attr_name:
            representation = attr_name
        if attr_name == pk:
            attrs.append("    %s = db.Column(%s, primary_key=True)" % (attr_name, attr_type))
        else:
            #FK
            if 'Id' in attr_name:
                attr_name_without_id = attr_name[:-2].lower()
                #specify FK
                if attr_name_without_id == 'order':
                    attr_name_without_id = 'torder'
                attrs.append("    %s = db.Column(%s, db.ForeignKey('%s.id'))" % (attr_name,
                                                                                 attr_type, attr_name_without_id))
                attrs.append("    %s = db.relationship('%s', primaryjoin='%s.id==%s.%s')" % (attr_name_without_id,
                                                                                             attr_name_without_id.capitalize(),
                                                                                             attr_name_without_id.capitalize(),
                                                                                             class_name, attr_name))
            else:
                attrs.append("    %s = db.Column(%s)" % (attr_name, attr_type))
    attrs = '\n'.join(attrs)

    if not representation:
        representation = 'str(self.id)'
    else:
        representation = 'self.%s' % representation
    repr_function = '\n\n'
    repr_function += "    def __repr__(self):\n"
    repr_function += "        return %s\n" % representation

    category_function = '\n'
    category_function += '    @classmethod\n'
    category_function += "    def category(cls):\n"
    category_function += "        return u'%s'\n" % category

    name_function = '\n'
    name_function += '    @classmethod\n'
    name_function += "    def name(cls):\n"
    name_function += "        return u'%s'\n" % name

    desc_function = '\n'
    desc_function += '    @classmethod\n'
    desc_function += "    def desc(cls):\n"
    desc_function += "        return u'%s'" % desc

    class_lines = "class %s(db.Model):\n" % class_name
    class_lines += attrs
    class_lines += repr_function
    class_lines += category_function
    class_lines += name_function
    class_lines += desc_function
    return "'%s'" % class_name, class_lines

comment_flag = False
current_op = None
content_stack = []
output_classes = []
output_names = []

for line in sql_lines:
    line = line.strip()

    #empty
    if not line:
        continue

    #comment
    if line.startswith(COMMENT_LINE):
        continue
    if line.endswith(COMMENT_PAIRS['END']):
        comment_flag = not comment_flag
        continue
    if comment_flag or line.startswith(COMMENT_PAIRS['START']):
        comment_flag = True
        continue

    #operation
    if not current_op:
        tokens = line.split()
        current_op = tokens[0]
        assert current_op in OPS, 'what operation? -- %s' % current_op
    content_stack.append(line)
    if line.endswith(';'):
        name, output = op_handler(current_op.lower(), content_stack)
        if name and output:
            output_names.append(name)
            output_classes.append(output)
        content_stack = []
        current_op = None

#output to py
f = codecs.open('auto_model.py', 'w', encoding='utf-8')
f.write('# -*- coding: utf-8 -*-\n\n')
f.write('from model import User\n')
f.write('from app import db\n\n')
f.write('__all__ = [%s]\n\n\n' % ', '.join(output_names))
f.write('\n\n\n'.join(output_classes))
f.close()
