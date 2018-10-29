#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 22:35
# @Author  : hellozjf
# @Email   : 908686171@qq.com
# @File    : Screen.py
# @Software: PyCharm


class Screen(object):

    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__resolution = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        self.__resolution = self.__height * self.__width
        return self.__resolution


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

