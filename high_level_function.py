#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 15:50
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : high_level_function.py
# @Software: PyCharm

from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add2(x, y):
    return x + y


print(reduce(add2, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


def normalize(name):
    if (len(name) == 0):
        return ""
    else:
        upper = str(name[:1]).upper()
        lower = str(name[1:]).lower()
        return upper + lower


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def mul(a, b):
    return a * b


def prod(L):
    return reduce(mul, iter(L))


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

m = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2Num(s):
    return m[s]


def tenPlus(a, b):
    return a * 10 + b


def str2float(s):
    pointIndex = s.index(".")
    if pointIndex != -1:
        # 说明有小数点，那就整数部分map-reduce一次，小数部分也map-reduce一次
        intString = s[:pointIndex]
        pointString = s[pointIndex + 1:]
        intValue = reduce(tenPlus, map(str2Num, intString))
        pointValue = reduce(tenPlus, map(str2Num, pointString))
        while pointValue > 1:
            pointValue /= 10
        return intValue + pointValue
    else:
        return reduce(tenPlus, map(str2Num, s))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
