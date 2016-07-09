#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
字符串
写一个函数，返回一个跟输入字符串相似的字符串，要求字符串的大小写反转.
比如输入'Mr.Ed'，应该返回'mR.eD'
'''

__author__ = 'Jackie Qiang'

def reStr(str):
    for i in range(len(str)):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            str = str[:i] + chr(ord(str[i])+32) + str[i+1:]    #无法改变str的值，因为str是不可变类型
        elif ord(str[i]) >= 97 and ord(str[i]) <=122:
            str = str[:i] + chr(ord(str[i])-32) +str[i+1:]
    return str

if __name__ == '__main__':
    str = input('请输入一条字符串')
    print(reStr(str))
