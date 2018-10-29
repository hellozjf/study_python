#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 13:43
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : function_recursive.py
# @Software: PyCharm


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(100))


# 使用尾递归
def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 讲道理，尾递归可以优化的，比方说fact2(5)会变成
# fact_iter(5, 1) -> fact_iter(4, 5) -> fact_iter(3, 20) -> fact_iter(2, 60) -> fact_iter(1, 120)，最后返回120
# 但实际上CPython解释器没有进行优化，所以还是存在栈溢出问题
# print(fact2(1000))


# 汉诺塔，它接收参数n表示第一个柱子的盘子数量，a、b、c分别是三个柱子的名称
def move(n, a, b, c):
    if (n == 1):
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
