#!/bin/usr/env python3
# -*- coding:utf-8 -*-
'''
模块研究
提取模块信息，提示用户输入一个模块名。然后使用dir()和其他内建函数提取模块的属性，显示他们的名字、类型、值
'''
__author__ = 'Jackie Qiang'

def show_module(name):
    obj = __import__(name)
    for item in dir(obj):
        print('name:%s' % item)
        print('type:%s' % type(getattr(obj,item)))
        print('value:%s' % getattr(obj,item))
    return True

if __name__ == '__main__':
    name = input('请输入一个模块名：')
    show_module(name)
