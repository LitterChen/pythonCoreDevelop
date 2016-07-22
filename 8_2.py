#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
循环
编写一个程序，让用户输入3个数字：from,to,increment.以increment为步长，从f开始计数到t，包括f和t。例如输入的f=2，t=26,i=4.程序将输出2,6,10,14,18,22,26
'''
__author__ = 'Jackie Qiang'
def recyle(ins):
    string = ins.split(' ')
    a = [int(i) for i in range(int(string[0]),int(string[1]),int(string[2]))]
    a.append(int(string[1]))
    return a
if __name__ == '__main__':
    ins = input('输入from,to,increment：')
    print(recyle(ins))
