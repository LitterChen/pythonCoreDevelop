#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
多列输出。有任意项的序列或者其他容器，把它们等距离分列显示。由调用者提供数据和输出格式。例如，如果你传入100个项并定义3列输出，按照需要的模式显示这些数据。这种情况下，赢是两列显示33个项，最后一列显示34个项。你可以让用户选择水平排序或者垂直排序
'''

__author__ = 'Jackie Qiang'

def multi_output(L,num,type = 1):
    number = int(len(L)/int(num))
    #垂直排序
    if type == 1:
        LS = []
        for i in range(num):
            LS.append([L[i+num*j] for j in range(number)])
        for i in range(1,len(L)-num*number+1):
            LS[num-1].append(L[num*number+i-1])
    #水平排序
    elif type == 2:
        LS = [L[i*number:i*number+number] for i in range(num-1)]
        LS.append(L[number*(num-1):])
    return LS
if __name__ == '__main__':
    L = [i for i in range(100)]
    result = multi_output(L,8,1)
    print(result)
    for i in range(len(result)):
        for j in range(int(len(result[i]))):
            print('%3d' % result[i][j],end='')
        print('')

