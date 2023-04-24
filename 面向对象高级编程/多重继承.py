#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


class Animal(object):
    pass

# 大类


class Mammal(Animal):
    pass


class Bird(Animal):
    pass

# 行为


class Runnable(object):
    def run(self):
        print('Running....')


class Flyable(object):
    def fly(self):
        print('Flying....')


# 各种动物


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass
