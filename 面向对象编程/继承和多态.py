#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
cat = Cat()

dog.run()
cat.run()

a = list()  # a 是list类型
b = Animal()  # b 是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())
