#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'


# class FooError(ValueError):
#     pass


# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n


# foo('0')


from functools import reduce


def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return sum(ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
