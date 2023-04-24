#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


# class Student(object):
#     def get_score(self):
#         return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integger')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100!')
#         self._score = value

""" 
s = Student()
s.set_score(60) 
print(s.get_score())

s.set_score(9999)
"""


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integger')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s = Student()
s.score = 60  # 实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()

# s.score = 9999


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
