#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
c.上面的例子，计算出此人下次生日还有多少天
'''

__author__ = 'Jackie Qiang'
import time
def nextB(date1):
    date = time.localtime();date1 = date1.split('/')
    if int(date1[1])>date[1]:
        date1[0] = str(date[0])
    elif int(date1[1])==date[1]:
        if int(date1[2])>=date[2]:
            date1[0] = str(date[0])
        else:
            date1[0] = str(date[0]+1)
    else:
        date1[0] = str(date[0]+1)
    date1 = '/'.join(date1)
    date2 = time.mktime(time.strptime(date1,'%Y/%m/%d'))
    date11 = time.time()
    return str(int((date2-date11)/86400)) + '天'

if __name__ == '__main__':
    date1 = input('input you birthday(like YYYY/MM/DD):')
    print(nextB(date1))
