# -*- coding: utf-8 -*-

from collections.abc import Iterable

print(isinstance('abc', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3, 4], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代


# 下标for循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min, max)


def findMinAndMax(L):
    if L:
        return (min(L), max(L))
    else:
        return (None, None)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
