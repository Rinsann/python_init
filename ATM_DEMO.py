#!/usr/bin/env python3
# -*- coding: utf-8 -*-

money = 5000000
name = input('请输入姓名: ')


def query(show_header):
    if show_header:
        print('======查询余额=====')
    print(f'{name},你的余额剩余:{money}')


def saving(num):
    global money
    money += num
    print('======存款=====')
    print(f'存入{num}元,目前余额为:{money}')


def get_money(num):
    global money
    money -= num
    print(f'取出{name}元,你的余额剩余:{money}')


def main():
    print('======主菜单=====')
    print(f'{name},你好,还有来到ATM,请选择操作')
    print('查询余额\t[输入1]')
    print('存款\t\t[输入2]')
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return int(input('请输入数字,选择操作'))


while True:
    keyboard = main()
    match keyboard:
        case 1:
            query(True)
            continue  # 通过continue继续下一次循环,一进来就进入主菜单
        case 2:
            num = int(input('请输入需要存入的金额: '))
            saving(num)
            continue
        case 3:
            num = int(input('请输入需要取出的金额: '))
            get_money(num)
            continue
        case 4:
            print('程序退出')
            break
