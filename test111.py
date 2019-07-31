#!/usr/bin/env python
# -*- coding: utf-8 -*-

import locale
import sys


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(7))

line = [1, 2, 3, 4, 5, 6]


def how_many_in(lst):
    if lst[1:]:
        print('me and the guys behind')
        return 1 + how_many_in(lst[1:])
    else:
        print('just me')
        return 1


how_many_in(line)

if __name__ == '__main__':
    print('hello world!')
    print('您好，世界！')

x = 1
print(id(x))
x = 2
print(id(x))
print(type(x))

s = '小甲'
print(s)
print(type(s))
print(sys.getdefaultencoding())
print(locale.getdefaultlocale())
with open('utf1', 'r+', encoding='utf-8') as f:
    f.write(s)
    print(f.read(-1))
# with open('gbk1', 'w', encoding='gbk') as f:
#     f.write(s)
# with open('jis1', 'w', encoding='shift-jis') as f:
#     f.write(s)
