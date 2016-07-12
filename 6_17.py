#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
方法：实现一个MyPop()函数,功能类似与Pop()，用一个列表作为输入，移除列表的最新一个元素，并返回它
'''

__author__ = 'Jackie Qiang'

def MyPop(L):
    L = L.split(' ')
    length = len(L)
    result = L[length-1]
    del L[length-1]
    return result

if __name__ == '__main__':
    L = input('输入列表：')
    print(MyPop(L))
