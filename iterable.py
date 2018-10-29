#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 14:24
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : iterable.py
# @Software: PyCharm

from collections import Iterable
import sys

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax2(L):
    if (len(L) == 0):
        return (None, None)
    # python3中最大最小的int值参考https://www.techforgeek.info/python_max_min_int.html
    min = sys.maxsize
    max = -sys.maxsize-1
    for i in L:
        if (i < min):
            min = i
        if (i > max):
            max = i
    return (min, max)


def findMinAndMax(L):
    if (len(L) == 0):
        return (None, None)
    else:
        return (min(L), max(L))


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

