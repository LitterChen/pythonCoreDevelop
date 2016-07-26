#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文件过滤
提示输入数字N和文件F,然后显示文件F的前N行。
'''
__author__ = 'Jackie Qiang'
if __name__ == '__main__':
    F = input('请输入文件名:')
    N = input('请输入要输出到第几行：')
    f = open(F,'r')
    n = 0
    for eachLine in f:
        if n == int(N):
            break
        else:
            print(eachLine,)
        n += 1
    f.close()
