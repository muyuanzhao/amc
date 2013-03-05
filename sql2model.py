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
    repr_funtion = '\n\n'
    repr_funtion += "    def __repr__(self):\n"
    repr_funtion += "        return %s\n" % representation

    category_funtion = '\n'
    category_funtion += '    @classmethod\n'
    category_funtion += "    def category(cls):\n"
    category_funtion += "        return u'%s'" % category

    class_lines = "class %s(db.Model):\n" % class_name
    class_lines += attrs
    class_lines += repr_funtion
    class_lines += category_funtion
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
f.write('from app import db\n\n')
f.write('__all__ = [%s]\n\n\n' % ', '.join(output_names))
f.write('\n\n\n'.join(output_classes))
f.close()
