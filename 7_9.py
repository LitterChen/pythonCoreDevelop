#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
翻译
字符串翻译程序（功能类似与Unix中的tr命令） 我们也使用tr来命名我们的函数
tr(srcstr,dststr,string) 将string中srctr替换为dststr
1. uplo 是否区分大小写 1.区分 0.不区分
'''
__author__ = 'Jackie Qiang'
import string
def tr(srcstr,dststr,string,uplo):
    pstring=string.lower()
    time = 0
    slen = len(srcstr)
    st_index = 0
    while True:
        try:
            if uplo == '1':
                strindex = string[st_index:].index(srcstr)
            else:
                strindex = pstring[st_index:].index(srcstr.lower())
            string = string[:strindex]+dststr+string[strindex+slen:]
            st_index = strindex+slen
            time += 1
        except ValueError: 
            break
    print('已经查找完毕!共有%d处被替换'% time)
    print('替换的句子\n%s'% string)
    return True
if __name__ == '__main__':
    string = input('请输入字符串：')
    srcstr = input('请输入查找的字符串：')
    dststr = input('请输入替换的字符串：')
    uplo = input('是否区分大小写 1.区分 0.不区分')
    tr(srcstr,dststr,string,uplo)
