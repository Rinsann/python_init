my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = my_list[1:4]
print(f"结果1是{result1}")


my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result2 = my_tuple[:]  # 起始和结束不写,默认从头到尾
print(f"结果2是{result2}")

my_str = '123456'
result3 = my_str[::2]
print(f"结果3是{result3}")


my_str = '012345678'
result4 = my_str[::-1]
print(f"结果4是{result4}")


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result5 = my_list[3:1:-1]
print(f"结果5是{result5}")


my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result6 = my_tuple[::-2]
print(f"结果6是{result6}")


my_str = 'php,++c-,c,avaj,nohtyp'
result6 = my_str[::-1]
result = result6.replace('-', '')
result_list = result.split(',')

print(result_list[-2])
