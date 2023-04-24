# -*- coding: utf-8 -*-

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 2, 3, 4, 5, 6)
print(f())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i) 立即被执行,因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn


f = inc()
print(f())  # 1
print(f())  # 2


def createCounter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
