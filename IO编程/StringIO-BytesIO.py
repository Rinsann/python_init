#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rin'

from io import StringIO, BytesIO
# f = StringIO()
# print(f.write('Hello'))
# print(f.write(' '))
# print(f.write('World!'))

# print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f2 = BytesIO()
print(f2.write('中文'.encode('utf-8')))
print(f2.getvalue())
