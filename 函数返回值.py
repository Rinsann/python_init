def add(a, b):
    result = a + b
    return result


r = add(124, 65)
print(r)


def check_age(age):
    if age > 18:
        return 'SUCCESS'
    else:
        return None


result = check_age(16)
if not result:
    print('未成年,不可以进入')


def add(x, y):
    """
      add函数可以接受两个参数,进行两数相加的功能
      :param x: 数字1
      :param y: 数字2
      :return: 返回两数相加的结果
    """
    result = x+y
    print(f'2数相加的结果是: {result}')
    return result


add(5, 7)
