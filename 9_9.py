#!/bin/usr/env python3
# -*- coding:utf-8 -*-
'''
Python文档字符串
进入Python标准库所在目录。检查每个.py文件看是否有_doc_字符串，如果有，对其格式进行适当的整理归类。你的程序执行完毕后，应该会生成一个漂亮的清单。里边列出那些模块又文档字符串，以及文档字符串的内容，清单最后附上那些没有文档字符串模块的名字
*提取标准库中歌模块内全部类和函数的文档
'''
__author__ = 'Jackie Qiang'
import os
def show_doc(path):
    f = open('/home/jackie/py','w')
    f.write('文档包括以下这些内容：\n')
    temp = []
    for parent,localdir,filenames in os.walk(path):
        for file in filenames:
            print(filenames)
            if '__doc__' in dir(file):
                f.write(file+':'+file.__doc__+os.linesep)
            else:
                temp.append(file)
    f.write('__doc__ not in there files:'+os.linesep)
    for i in temp:
        f.write(i+os.linesep)
    return True

if __name__ == '__main__':
    path = input('标准库的位置:')
    show_doc(path)
