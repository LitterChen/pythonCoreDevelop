#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
随机数
使用random模块中的randint()方法生成一个随机数集合，从0到9中随机选择，生成1~10个随机数
每次生成集合A和集合B后，显示结果 A|B和 A&B
'''
__author__ = 'Jackie Qiang'
import random
def setT():
    seta = set([random.randint(0,9) for i in range(random.randint(0,9))])
    setb = set([random.randint(0,9) for i in range(random.randint(0,9))])
    print('A是%s\nB是%s\nA|B:%s\nA&B:%s'%(seta,setb,seta|setb,seta&setb))

if __name__ == '__main__':
    setT()
