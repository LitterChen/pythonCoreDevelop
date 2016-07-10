#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
制作一个简单的锤子，剪刀，布游戏。用户输入一个，电脑随机生成一个。最后返回判断的结果
'''
__author__ = 'Jackie Qiang'
import random
def game(str):
    unum = int(str)
    cnum = random.randint(0,2)
    hand = {0:'锤子',1:'剪刀',2:'布'}
    print('你出了%s，电脑出了%s' % (hand[unum],hand[cnum]))
    result = unum-cnum
    if not result:
         results = '平局'
    elif abs(result)>1:
          results = 'you win' if result>0 else 'you lose'
    else:
          results = 'you win' if result<0 else 'you lose'
    return results

if __name__ == '__main__':
    str = input('输入猜拳 0.锤子 1.剪刀 2.布')
    print(game(str))
