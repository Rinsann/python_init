# -*- coding: utf-8 -*-


import functools
print(int('12345'))

print(int('123456', base=8))


print(int('123456', base=16))


def int2(x, base=2):
    return int(x, base)


print(int2('1000000000'))
print(int2('10101010'))


int2 = functools.partial(int, base=2)
print(int2('100000000'))
print(int2('0101010'))
