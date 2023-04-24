#!/usr/bin/env python3
# -*- coding: utf-8 -*-
money = 10000

for i in range(1, 21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效分{score},不满足,没有奖金,下一位")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}绩效分{score},满足,奖金1000,剩余{money}")
    else:
        print(f'余额不足,当前余额:{money}元,下个月补发')
        break
