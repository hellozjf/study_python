#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 21:31
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : partial.py
# @Software: PyCharm

import functools


int2 = functools.partial(int, base=2)


print(int2('1000000'))
print(int2('1010101'))
