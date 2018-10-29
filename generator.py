#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 14:53
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : generator.py
# @Software: PyCharm


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        # yield关键字令fib从普通的函数变为generator了
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
for t in f:
    print(t)


def triangles2():
    list = [1]
    list2 = []
    n = 1
    while True:
        i = 0
        while i <= n:
            if i == 0:
                list2.append(list[i])
            elif i == n:
                list2.append(list[n - 1])
            else:
                list2.append(list[i - 1] + list[i])
            i = i + 1
        yield list
        list = list2.copy()
        list2.clear()
        n = n + 1


def triangles():
    li = [1]
    while True:
        yield li
        # 如果list一开始是[1]，则将它变为[0, 1]
        list1 = li.copy()
        list1.insert(0, 0)
        # 如果list一开始是[1]，则将它变为[1, 0]
        list2 = li.copy()
        list2.append(0)
        # list1 + list2就是新的list
        # print('list1 =', list1, 'list2 =', list2)
        i = 0
        size = len(li) + 1
        li = []
        while i < size:
            li.append(list1[i] + list2[i])
            i = i + 1


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
    print(results)
