#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict, Counter

x = OrderedDict(a=1, c=3, b=2)
y = Counter('Hello World!')
print(x)
print(y)

if __name__ == '__main__':
    print('hello world!')
    print('您好，世界！')

'''
Example for kinds of data structure
In order to learn them quickly
'''

# Bool
print()
print('Bool:')
print(int(True))
print(bool(100))

print()
x = [True, True, False]
if any(x):
    print('at least one True')
if all(x):
    print('not one False')
if any(x) and not all(x):
    print('at least one True and one False')
print(f'dir : {dir(x)}')

# List: can modify
print()
print('List:')
names_python_pc = ['陈升', '刘德华', '杨幂', 'TFboys']
names_python_pc.append('F4')
print(f'Python实战圈的成员有：{names_python_pc}')
print(f'Python实战圈的成员有：{names_python_pc[1]}')
print(f'type: {type(names_python_pc)}')

# Tuple: cannot modify
print()
print('Tuple:')
tup1 = (1, 2, 3)
print(tup1)

# Dictionary: can modify
print()
print('Dictionary:')
name_dictionary = {'魏璎珞': 300, '皇后': {'male': False}, '皇贵妃': (100, 200, 250.5), '贵妃': ['female', 35], '斌': 'NA'}
print(name_dictionary)
print('value: {}'.format(name_dictionary.values()))
print('皇贵妃: {}'.format(name_dictionary.get('皇后').get('male')))

# for
print()
print('For:')
for x in range(0, 11):
    if x == 0:
        pass
    elif x == 1:
        continue
        print('continue')
    elif x == 8:
        break
        print('break')
    else:
        pass
    print(x)

# set
a = {1, 2, 3}
b = {2, 5, 8, 10}
print(f'set intersection: {a.intersection(b)}')
print(f'set difference: {a.difference(b)}')
print(f'set union: {a.union(b)}')
print(f'type of a: {type(a)}')

# function
print()
print('Function:')


def new_function(my_value='test'):
    print(f'this is a new function: {my_value}')


new_function()
new_function('hello world')

# lambda
print()
print('Lambda:')
aa = [1, 2, 3]
y = map(lambda bb: bb + 1, aa)
print(list(y))
# def my_lambda(): lambda a1, b1, c1: a1 - 200 + b1 - c1
# my_lambda(100, 100, 100)
