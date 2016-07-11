#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
a.给出两个可识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY格式，计算出两个日期间的天数
'''

__author__ = 'Jackie Qiang'
import time
def calD(date1,date2):
    date11 = date1.split('/');date22 = date2.split('/')
    for i in range(len(date11)):
        if date11[i] != date22[i]:
            if date11[i]<date22[i]:
                date1,date2 = date2,date1
            break;
    date1 = time.mktime(time.strptime(date1,'%Y/%m/%d'));date2 = time.mktime(time.strptime(date2,'%Y/%m/%d'))
    return str(int((date1-date2)/86400)) + '天'

if __name__ == '__main__':
    date1 = input('input first date,like YYYY/MM/DD')
    date2 = input('input last date,like YYYY/MM/DD')
    print(calD(date1,date2))
