#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


class Student(object):
    name = 'Student'

    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90

print(s.name)


# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
