#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check():
    print('扫描乘车')


def add(a, b, z):
    result = (a+b)*z
    print(f"{a}+{b}*{z}={result}")


add(13, 46, 2)


def check_money(money):
    print('扫描乘车')
    if money >= 2:
        print(f'欢迎乘车')
    else:
        print('余额不足请充值')


check_money(2)
