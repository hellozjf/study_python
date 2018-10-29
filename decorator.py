#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 18:45
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : decorator.py
# @Software: PyCharm

import time
import functools
import datetime


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()
# 这里会打印出wrapper，所以后面的代码需要@functools.wraps，以便纠正func.__name__
print(now.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()
print(now.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        now_time = datetime.datetime.now()
        print('now_time =', now_time)
        result = fn(*args, **kw)
        last = datetime.datetime.now() - now_time
        print('%s executed in %d.%06d s' % (fn.__name__, last.seconds, last.microseconds))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    print('before time.sleep(0.0012)')
    time.sleep(0.0012)
    print('after time.sleep(0.0012)')
    return x + y


@metric
def slow(x, y, z):
    print('before time.sleep(0.1234)')
    time.sleep(0.1234)
    print('after time.sleep(0.1234)')
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')

