#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'

import os

# 获取当前工作目录的路径
current_dir = os.getcwd()

# try:
#     f = open('D:\\MyProject\\React_DEMO\\python_demo\\IO编程\\test.txt',
#              'r', encoding='gbk', errors='ignore')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 简化写法
with open(os.path.join(current_dir, 'IO编程/test.txt'), 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

# for line in f.readlines():
#     print(line.strip())  # 把末尾的 '\n' 删掉

with open(os.path.join(current_dir, 'IO编程/test.txt'), 'a', encoding='gbk', errors='ignore') as f:
    f.write('Hello World!')
