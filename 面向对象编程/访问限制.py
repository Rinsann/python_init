#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self._score = new_score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self._name, self._score))


# bart = Student('Bart Simpson', 69)
# bart.__name


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        # if gender == 'female' or gender == 'male':
        if gender in ['female', 'male']:
            self.gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
