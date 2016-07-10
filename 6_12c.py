#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
c.创建一个名字为findchr()函数，函数声明如下 def subdchr(string,orichr,newchr) 要求在
string中找到chr，并用新串代替。同时返回新字符串，否则返回-1
'''
__author__ = 'Jackie Qiang'
def subchr(string,orichr,newchr):
    change = 0;
    for i in range(len(string)):
        if string[i] == orichr:
            string = '%s%s%s' % (string[:i],newchr,string[i+1:])
            change = 1
    if change:
        return string
    else:
        return -1

if __name__ == '__main__':
    string = input('请输入待查找字符串')
    chr = input('请输入一个需要查找的字符')
    newchr = input('请输入要替换的字符')
    print(subchr(string,chr,newchr))

