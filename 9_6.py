#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文件比较
写一个比较两个文本文件的程序，如果不同，给出第一个不同出的行号和列号
'''
__author__ = 'Jackie Qiang'
def comparefile(filepath1,filepath2):
    f1 = open(filepath1)
    f2 = open(filepath2)
    count_line = 0
    for line1,line2 in zip(f1,f2):
        count_line += 1
        if line1 != line2:
            count_list = 0
            for i,j in zip(line1,line2):
                count_list += 1
                if i != j:
                    print('The diffrent is %d line and %d list' % (count_line,count_list))
                    break
            if count_list != 0:
                break
if __name__=='__main__':
    filepath1 = input(r'Please input first file path:')
    filepath2 = input(r'Please input second file path:')
    comparefile(filepath1,filepath2)
    print('Done!')
