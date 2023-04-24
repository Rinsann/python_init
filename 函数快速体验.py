#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str1 = 'utf-8'
str2 = 'gbk'
str3 = 'gb2312'

count = 0
for i in str1:
    count += 1
print(f'{str1}的长度是{count}')


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f'{data}的长度是{count}')


my_len(str1)
my_len(str2)
my_len(str3)
