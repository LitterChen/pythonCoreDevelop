#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
转换
接受分钟数，返回小时数和分钟数。总时间不变，要求小时数经可能的大
'''

__author__ = 'Jackie Qiang'

def m2h(mins):
    try:
        mins = int(mins)
    except (TypeError,ValueError):
        print('输入有误！请输入整数分钟数.')
        return None
    hour = int(mins/60)
    mins = mins%60
    time =str(hour) + ' 小时 '+ str(mins) +' 分钟'
    return time

if __name__ == '__main__':
    mins = input('请输入整数分钟数')
    print(m2h(mins))
