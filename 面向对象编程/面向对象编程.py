#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'

std1 = {'name': 'rin', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
