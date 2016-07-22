#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文本处理
要求输入一个姓名列表，输入格式是"Last name,First name"
如果用户输入错误，请你纠正它。并告知用户，同时你还需要记录输入错误的次数
'''
__author__ = 'Jackie Qiang'
def nameList(num):
    error = 0
    name = []
    for i in range(num):
        a = input('Please enter name %d:' % i)
        if len(a.split(' ')) == 2:
            b = a.split(' ')
            a = ','.join(sorted(b,reverse=True))
            error += 1
            print('Wrong format... should be Last,First.')
            print('you have done this %d time(s) already.Fixing input...' % error)
        name.append(a) 
    print('The sorted list (by last name) is:')
    for i in sorted(name,reverse=True):
        print(i)
    return True

if __name__ == '__main__':
    num = input('请输入你要填写的名字个数:')
    nameList(int(num))
