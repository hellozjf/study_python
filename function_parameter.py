#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 13:11
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : function_parameter.py
# @Software: PyCharm


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))
print(power(5, 3))
print(power(5))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
# 下面三行代码告诉我们，默认参数必须指向不变对象，否则会有问题
print(add_end())
print(add_end())
print(add_end())


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
print(calc())

nums = [1, 2, 3]
# *nums将数组转化为可变参数
print(calc(*nums))


# 除name和age外，其它参数会存放在kw中
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# 注意，改变person函数里面的kw变量，不会影响extra变量
person('Jack', 24, **extra)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


def product(*x):
    if (len(x) == 0):
        raise TypeError('argument length == 0')
    result = 1
    for t in x:
        result *= t
    return result


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
