#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
阶乘
返回一个数的阶乘
'''
__author__ = 'Jackie Qiang'
from functools import reduce
def factorial(num):
    sum = 0
    return reduce(lambda x, y : x * y, range(1,num+1))
if __name__ == '__main__':
    num = input('一个要阶乘的数：')
    print(factorial(int(num)))
