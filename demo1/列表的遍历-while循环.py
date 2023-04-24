def list_while_func():
    my_list = ['你的名字', '言叶之庭', '你好世界']

    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f'第{index}个元素是 {element}')
        index += 1


def list_for_func():
    my_list = ['你的名字', '言叶之庭', '你好世界']
    for element in my_list:
        print(element)


list_while_func()
list_for_func()


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
new_list = []
""" while index < len(list):
    if list[index] % 2 == 0:
        new_list.append(list[index])
    index += 1 """


for i in list:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)
