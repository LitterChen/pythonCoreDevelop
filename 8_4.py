#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
素数
我们在本章已经给出了一些代码来确定一个数字的最大约数或者是否是一个素数。请把相关代码转换为一个返回值为布尔值的函数，函数名为isprime()。如果输入的是一个素数。那么返回True，否则返回False。
'''
__author__ = 'Jackie Qiang'
def isprime(num):
    '现在使用的是穷举法，和本身之前的所有数进行余数运算'
    for i in range(2,num):
        if not num%i:
            print('约数为%d' % i)
            return False
    return True

if __name__ == '__main__':
    num = input('请输入一个数字来判断它是否为素数:')
    print(isprime(int(num)))
