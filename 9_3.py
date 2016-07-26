#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文件信息
提示输入一个文件名，显示这个文本文件的总行数
'''
__author__ = 'Jackie Qiang'
if __name__ == '__main__':
    F = input('请输入要打开的文件名:')
    f = open(F,'r')
    l = len(f.readlines())
    f.close()
    print('共有%d行'% l)
