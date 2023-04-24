def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# print(power(5, 2))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)


# enroll('Sarah', 'F')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# print(add_end([1, 2, 3]))
# print(add_end())


# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# print(calc(1, 2))

nums = [1, 2, 3, 4]
# print(calc(*nums))


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(person('Michael', 30, **extra))


# 命名关键字参数
def person(name, age, *, city='Shanghai', job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


# person('Jack', 24,  job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


""" f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None) """

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 计算两个数的乘积,改造成可接收一个或多个数并计算乘积


def mul(*args):
    if len(args) == 0:
        raise TypeError
    elif len(args) == 1:
        return args[0]
    else:
        result = 1
        for i in args:
            result *= i
        return result


print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
