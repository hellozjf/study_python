#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight / (height * height)
print('bmi =', bmi)
if bmi > 32:
    print('过轻')
elif 18.5 <= bmi and bmi < 25:
    print('正常')
elif 25 <= bmi and bmi < 28:
    print('过重')
elif 28 <= bmi and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
