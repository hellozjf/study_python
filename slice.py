#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 13:59
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : slice.py.py
# @Software: PyCharm

L = list(range(100))
# 前10个数
print(L[:10])
# 最后10个数
print(L[-10:])
# 前11-20个数
print(L[10:20])
# 前10个数，每2个取一个
print(L[:10:2])
# 所有数，每5个取一个
print(L[::5])
# 原样复制一个List
print(L[:])


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim2(s):
    if (len(s) == 0):
        return ''
    # print(s)
    # 首先从字符串头部开始，统计有多少个空格
    startIndex = 0
    while (startIndex < len(s) and s[startIndex] == ' '):
        startIndex = startIndex + 1
    # 然后从字符串尾部开始，统计有多少个空格
    endIndex = len(s) - 1
    while (endIndex >= 0 and s[endIndex] == ' '):
        endIndex = endIndex - 1
    # print('startIndex =', startIndex, 'endIndex =', endIndex)
    # print(s[startIndex:endIndex+1])
    if (startIndex <= endIndex):
        return s[startIndex:endIndex+1]
    else:
        return ''


def trim(s):
    if (len(s) == 0):
        return ''
    elif (s[0] == ' '):
        return trim(s[1:])
    elif (s[-1] == ' '):
        return trim(s[:-2])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
