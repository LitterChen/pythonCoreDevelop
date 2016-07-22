#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
素数
列举出1~10^3的所有素数.
能否更加简化？感觉是可以 用列表生成器？
'''
__author__ = 'Jackie Qiang'

if __name__ == '__main__':
    prime = [2]
    for i in range(3,10**3):
        x = 1
        for j in prime:
            if not i%j:
                x = 0
                break
        if x:
            prime.append(i)
    print(prime)
