#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
约数
完成一个名为getfactors()的函数。他接受一个整形作为参数，返回它所有约数的列表，包括1和本身
'''
__author__ = 'Jackie Qiang'
def getfactors(num):
    '现在使用的是穷举法，和本身之前的所有数进行余数运算'
    factors = []
    for i in range(1,num):
        if not num%i:
            factors.append(i)
    factors.append(num)
    return factors

if __name__ == '__main__':
    num = input('请输入一个数字求得它所有的约数:')
    print(getfactors(int(num)))
