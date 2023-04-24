# -*- coding: utf-8 -*-

from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


# print(add(-5, 6, abs))

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x+y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x*10+y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(fn, map(char2num, '13579'))

# 整理成一个str2int的函数就是：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x*10+y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int('13579'))


# 写个简化版本的
# char2num

def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))


# 练习
def normalize(name):
    return name.capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习
def prod(L):
    def mul(x, y):
        print(x, y)
        return x*y
    return reduce(mul, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(str):
    s = str.replace('.', '')
    num = 10 ** (len(str) - str.find('.') - 1)
    return reduce(lambda a, b: a * 10 + b, map(lambda v: int(v), s)) / num


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
