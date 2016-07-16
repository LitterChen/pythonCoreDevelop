#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
颠倒字典中的键和值
用一个字典做输入，输出另一个字典，用前者的键做值，值做键
'''
t1 = {chr(i):i for i in range(65,90)}
t2 = {i[1]:i[0] for i in t1.items()}
print(t2)
