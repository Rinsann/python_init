""" def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x """

# 参数类型检查


import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    if x >= 0:
        return x
    else:
        return -x


# print(my_abs('a'))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi/6)
# print(r)


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    if a == 0:
        return -c/b
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            return 'no answer'
        elif delta == 0:
            return -b/(2*a)
        else:
            return (-b+math.sqrt(delta))/(2*a), (-b-math.sqrt(delta))/(2*a)


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
