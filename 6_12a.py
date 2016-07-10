#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
a.创建一个名字为findchr()函数，函数声明如下 def findchr(string,chr) 要求在
string中找到chr。则返回索引，否则返回-1
'''
__author__ = 'Jackie Qiang'
def findchr(string,chr):
    for i in range(len(string)):
        if string[i] == chr:
            return i;
    return -1;

if __name__ == '__main__':
    string = input('请输入待查找字符串')
    chr = input('请输入一个需要查找的字母')
    print(findchr(string,chr))
