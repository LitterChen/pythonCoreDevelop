#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
完全数
如果一个数的约数（不包括它本身）之和等于他自己，那么就是完全数
'''
__author__ = 'Jackie Qiang'
def getfactors(num):
    factors = []
    for i in range(1,num):
        if not num%i:
            factors.append(i)
    return factors
def isPerfectNumber(num):
    factors = getfactors(num)
    sum = 0
    for i in factors:
        sum += i
    return True if sum==num else False
if __name__ == '__main__':
    num = input('请输入一个数字查看它是否是完全数:')
    print(isPerfectNumber(int(num)))
