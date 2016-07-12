#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
矩阵：处理矩阵M和N的加和乘操作
'''

__author__ = 'Jackie Qiang'
def ad(M,N):
    length = len(M[0]) #检验矩阵输入是否合法的参数
    #先检验自身，每一行的元素是否存在，不存在补0
    for i in range(len(M)):
        if len(M[i]) == length == len(N[i]):
            pass
        else:
            for j in range(length - len(M[i])):
                M[i].append(0)
            for j in range(length - len(N[i])):
                N[i].append(0)
    aM = []
    for i in range(len(M)):
        aM.append([])
        for j in range(length):
            aM[i].append([])
            aM[i][j] = int(M[i][j])+int(N[i][j])
    return aM
def mut(M,N):
    length = len(M[0])
    #先检验自身，每一行的元素是否存在，不存在补0
    for i in range(len(M[0])):
        if len(M[0]) == length:
            for j in range(length - len(N[i])):
                N[i].append(0)
        else:
            for j in range(length - len(M[i])):
                M[i].append(0)
    for i in range(len(M[0])):
        if len(M[0]) == len(N):
            pass
        else:
            return None
    aM = []
    for i in range(len(M)):
        aM.append([])
        for j in range(len(N[0])):
            aM[i].append([])
            result = 0
            for k in range(length):
                result += int(M[i][k]) * int(N[k][j])
            aM[i][j] = result
    return aM
if __name__ == '__main__':
    i = '';M = [];N=[];
    while i!='q':
        i = input('输入M矩阵的行向量(每个元素用空格，结束新起一行输入q)')
        if i!='q':
            M.append(i.split(' '))
    i = ''
    while i!='q':
        i = input('输入N矩阵的行向量(每个元素用空格，结束新起一行输入q)')
        if i!='q':
            N.append(i.split(' '))
#    print('加法',ad(M,N))
    print('乘法',mut(M,N))

