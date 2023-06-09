#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


from enum import Enum, unique


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sum = 0  # Sun的value被设置为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)


# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
