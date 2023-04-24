#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types
__author__ = 'Rin'

print(type(123))
print(type(abs))

print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance((1, 2, 3), (list, tuple)))

print(dir('ABC'))
