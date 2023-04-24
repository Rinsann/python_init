#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType
__author__ = 'Rin'


class Student(object):
    __slots__ = ('name', 'age')  # 用 tuple 定义允许绑定的属性名称


s = Student()
s.name = 'Rin'
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(26)  # 调用实例方法
print(s.age)

s2 = Student()  # 创建新的实例
# s2.set_age(25)  # 调用方法


# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)


""" 
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。 
"""
