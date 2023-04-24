# -*- coding: utf-8 -*-

print(sorted([36, 5, -12, 9, -21]))

# 按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))


print(sorted(['bob', 'about', 'Zoo', 'Credit']))


# 忽略大小写排序

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)
print(L2)
