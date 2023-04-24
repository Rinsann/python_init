#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
