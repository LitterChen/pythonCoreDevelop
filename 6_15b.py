#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
b.给出一个人的生日，计算从此人出生到现在的天数，包括所有的闰月
'''

__author__ = 'Jackie Qiang'
import time
def calB(date1):
    date11 = time.time();date2 = time.mktime(time.strptime(date1,'%Y/%m/%d'))
    return str(int((date11-date2)/86400)) + '天'

if __name__ == '__main__':
    date1 = input('input you birthday(like YYYY/MM/DD):')
    print(calB(date1))
