#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
b.创建一个名字为rfindchr()函数，函数声明如下 def rfindchr(string,chr) 要求在
string中找到chr。则返回索引，否则返回-1,和第一题不同在于，它从后面开始查找
'''
__author__ = 'Jackie Qiang'

def rfindchr(string,chr):
    for i in range(len(string)):
        if string[-i-1] == chr:
            return len(string)-i-1;
    return -1;

if __name__ == '__main__':
    string = input('请输入待查找字符串')
    chr = input('请输入一个需要查找的字母')
    print(rfindchr(string,chr))
