#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 18:34
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : lambda.py
# @Software: PyCharm


# def is_odd(n):
#     return n % 2 == 1


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
