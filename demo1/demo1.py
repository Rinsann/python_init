"""
用 for 循环实现1~100的求和
"""
# sum = 0
# for x in range(101):
#     sum += x

# print(sum)

"""
用 for 循环实现1~100的偶数求和
"""


"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum) 
"""

# 猜数字游戏

""" 
import random
answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        break
print(f'你总共猜了{counter}次')
if counter > 7:
    print('你的智商余额明显不足')
"""

# 输出乘法口诀表

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i*j}', end='\t')
    print()
