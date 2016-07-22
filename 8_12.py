#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
位操作
用户编写一个程序，用户给出起始和结束数字后给出以下表格，显示出两个数字间的所有整型的十进制，二进制，16进制。如果字符可以打印，则打印出相应的ascll码
'''
__author__ = 'Jackie Qiang'
def bitOper(begin,end):
    print('DEC\tBIN\tOCT\tHEX')
    print('---------------------------------------')
    for i in range(int(begin),int(end)):
        print('%d\t%s\t%o\t%x\t%s'%(i,format(i, 'b'),i,i,chr(i)))
    return True

if __name__ == '__main__':
    begin = input('开始的数字:')
    end = input('结束的数字:')
    bitOper(begin,end)

