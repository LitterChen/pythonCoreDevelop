#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
人力资源
创建一个简单的雇员姓名和编号的程序，让用户输入一组雇员姓名和编号。
你的程序可以提供按照姓名排序输出的功能，雇员姓名显示再前面，后面是对应的编号
'''
worker = {}
def add():
    global worker
    name = input('输入雇员姓名:')
    Id = input('输入雇员编号:')
    try:
        worker.update({name:Id})
    except Exception:
        print('输入有误！')
        return None
    return True
def show_n():
    global worker
    try:
        for i in sorted(worker):
            print('姓名：%s|编号：%s' % (i,worker[i]))
    except Exception:
        print('无数据！')
        return None
    return True
def show_i():
    global worker
    print(worker)
    try:
        for i in sorted(worker.items(), key=lambda x: x[1]):
            print('姓名：%s|编号：%s' % (i[0],i[1]))
    except Exception:
        print('无数据！')
        return None
    return True
choice = {"a":add,'n':show_n,'i':show_i}
if __name__ == '__main__':
    q = True
    while q:
        ch = input('''
              ********员工管理系统*********
              输入a:添加员工信息
              输入n:按员工名字排序
              输入i:按员工编号排序
              输入q:退出''')
        q = False if ch == 'q' else True
        if q:
            try:
                choice[ch]()
            except TypeError:
                print('输入信息有误')

