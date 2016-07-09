#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
列表
给出一个整数型，返回代表该值的英文。比如输入89，返回“eight-nine”
'''

def num2str(num):
    try:
        num = int(num)
    except (ValueError,TypeError):
        print('请重新输入整数')
        return None
    chr= ('zero', 'one', 'two' ,'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    number = []
    while num>1:
        number.append(int(num%10))
        num /= 10
    str = ''
    for i in range(len(number)):
        if i!=0:
            str = '-' + str
        str = chr[number[i]] + str
    return str;

if __name__ == '__main__':
    num = input('请输入一个整数')
    print(num2str(num))
