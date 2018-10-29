#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 12:57
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : function.py.py
# @Software: PyCharm

import math

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


print(my_abs(-99))
# print(my_abs('A'))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    r1 = (-1 * b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    r2 = (-1 * b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return r1, r2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


