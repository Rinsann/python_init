# 声明这是python3文件,utf-8编码

""" my_str = 'ftsann and Python'
value = my_str[2]
value2 = my_str[-16]

print(f"从字符串{my_str}中取出下标为2的字符是{value}, 取出下标为-16的字符是{value2}")


value3 = my_str.index('and')
print(f"and在字符串{my_str}中的起始下标是{value3}")


new_my_str = my_str.replace('and', 'or')
print(f"将字符串{my_str}中的and替换为or后的结果是{new_my_str}") """


# my_str = ' hello world and Python '
# my_str_list = my_str.split(' ')
# print(f" 将字符串 {my_str} 按空格分割后的结果是 {my_str_list} ,类型是 {type(my_str_list)} ")

""" new_my_str = my_str.strip()
print(f"将字符串{my_str}去除两端空格后的结果是{new_my_str}.")

my_str = '21hello world and Python21'
new_my_str = my_str.strip('12')
print(f"将字符串{my_str}去除两端的1和2后的结果是{new_my_str}.") """

# 统计字符串中某个字符出现的次数
""" my_str = 'hello world and Python and hello world'
print(f"字符串{my_str}中字符o出现的次数是{my_str.count('o')}") """


# 统计字符串的长度
""" print(f"字符串{my_str}的长度是{len(my_str)}")


my_str = 'hello world and Python and hello world'
for i in my_str:
    print(i) """


my_str = 'hello world and Python and hello world'
my_str.count('o')
new_my_str = my_str.replace(' ', '|')
new_my_list_str = new_my_str.split('|')
print(new_my_str)
print(new_my_list_str)
