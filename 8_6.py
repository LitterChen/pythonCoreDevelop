#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
素因子分解
求素因子
'''
__author__ = 'Jackie Qiang'
def isprime(num):
    for i in range(2,num):
        if not num%i:
            return False
    return True
def getfactors(num):
    factors = []
    for i in range(2,num):
        if not num%i:
            factors.append(i)
    return factors
def getprime(num):
    prime = []
    if not isprime(num):
        prime += getfactors(num)
    else:
        return None
    result = []
    while num!=1:
        for i in prime:
            if not num%i:
                result.append(i)
                num /= i
                break
    return result

if __name__ == '__main__':
    num = input('请输入一个数字求素因子分解:')
    print(getprime(int(num)))
