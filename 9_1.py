#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文件过滤
显示一个文件的所有喊，忽略以#好开头的行
*处理不是第一个字符开头的注释
'''
__author__ = 'Jackie Qiang'
if __name__ == '__main__':
    filename = input('请输入要读出的文件名：')
    f = open(filename,'r')
    for eachLine in f:
        #if eachLine[0]=='#':
        if eachLine[0] == '#' and ord(eachLine[1])>47 and ord(eachLine[1])<58:  #*题
            continue
        else:
            print(eachLine)
    f.close()

