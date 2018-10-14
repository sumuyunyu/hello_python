#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 19:03
# @Author  : jxyxyj@gmail.com
# @Site    : 
# @File    : dictionary.py.py
# @Software: PyCharm
from copy import deepcopy
# 字典格式化字符串 用于 网页
template = '''
            <html>
                <head>%(title)s</head>
                <body>
                <p>%(text)s</p>
                </body>
            </html>'''
data = {'title': 'my home page', 'text': 'welcome to my home page'}

print(template % data)

# 浅赋值的问题

x= {}

x['name'] = 'jxy'
x['age'] = 12
y = x
x['name'] = 'none'
x = {}
y
# y 还是会输出none 和12

x= {}

x['name'] = 'jxy'
x['age'] = 12
y = x
x['name'] = 'none'
x.clear()
y
# y会输出空，所以一般用copy(),深copy 要用deepcopy()
x = {'username':'admin','machines':['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'min'
y['machines'].remove('bar')

x
# >>> x
#  {'machines': ['foo', 'baz'], 'username': 'admin'}


d = {}
d['name'] = ['afed', 'betand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('clibe')

# d
# {'name': ['afed', 'betand', 'clibe']}
# c
# {'name': ['afed', 'betand', 'clibe']}
# dc
# {'name': ['afed', 'betand']}

# 3 fromkeys
{}.fromkeys(['name', 'bertrand'])
# {}.fromkeys(['name', 'bertrand'])
# {'name': None, 'bertrand': None}
b = dict.fromkeys(['name', 'age'])
# 可以自己赋默认值
b = dict.fromkeys(['name', 'age'],'(unknown)')

# 4get
d = {}
# print(d['name'])
# 上式会出错
# 下式就不会
print(d.get('name'))
# 更宽松的访问字典的方法

labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

name = input('Name:')

request = input('p or a')
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 5 has_key 相当于 in
# 6 items 将字典所有想以列表的方式返回，但没有遵循特定的顺序。
d = {'username':'admin','machines':['foo', 'bar', 'baz']}
d.items()
# iteritems()会返回迭代器 iterator对象，而不是list 不过python3里面没了
# python只有这个了
it = d.__iter__()
# 把键以列表的形式返回
d.keys()
# 获得给定的值，并移除
d.pop('name')
d.popitem()# 会弹出随机项

d = {}
print(d.setdefault('name','N/A'))
d
# name有值，就不改变该值，没值就设个默认值 （None或其他）

# update() 利用一个字典更新另一个字典,新项会被添加，旧项会被覆盖

d.update(x)

#12  values itervalues以list的形式返回值。（keys是返回键）
