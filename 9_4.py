#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文件访问
写一个逐页显示文本文件的程序。提示输入一个文件名，每次显示文本文件的25行，zhanthd:
'''
__author__ = 'Jackie Qiang'
if __name__ == '__main__':
    count = 0
    F = input('请输入文件名:')
    f = open(F,'r')
    for eachLine in f:
        if count == 5:
            count = 0
            input('请按键继续...')
            continue
        else:
            count += 1
            print(eachLine,)
    f.close()
