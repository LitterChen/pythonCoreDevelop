#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
返回斐波那契数列
'''
__author__ = 'Jackie Qiang'
def fibonacci(num):
    if num==1: 
        return 1;
    else:
        i = 1
        parament1 = 1
        parament2 = 1
        while i != num-1:
            if i%2==1:
                parament1 += parament2
            else:
                parament2 += parament1
            i += 1
        if i % 2:
            return parament2
        else:
            return parament1 

if __name__ == '__main__':
    num = input('请输入要返回第几个斐波那契数：')
    print(fibonacci(int(num)))
