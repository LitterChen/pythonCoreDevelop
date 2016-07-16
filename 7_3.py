#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
字典和列表方法
1.创建一个字典，并把这个字典中的键按照字母顺序显示出来
2.按照字母顺序排序好的键，显示出这个字典中的键和值
3.按照字母顺序排序好的值，显示出这个字典的键和值
'''
import random
test1 = {chr(i):random.uniform(0,i) for i in range(65,90)}
#'键'
for i in sorted(test1.items()):
    print('键：%s,值：%s'% (i[0],i[1]))
#'值'  注意这里的key函数
for i in sorted(test1.items(), key=lambda x: x[1]):
    print('键：%s,值：%s'% (i[0],i[1]))
