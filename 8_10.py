#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
文本处理。统计一句话中的元音，辅音及单词（以空格分割）的个数
×考虑元音和辅音的特殊情况，如"h","y","qu"等
'''
__author__ = 'Jackie Qiang'
def countChr(string):
    vowelNum = 0;consoment = 0
    vowel = ('a','e','i','o','u','A','E','I','O','U')

    chrNum = len(list(filter(lambda x:x!='',string.split(' ')))) #如果出现多个空格情况，可以考虑使用正则表达式。没有考虑字母中加其他字符的情况
    for i in string:
        if i in vowel:
            vowelNum += 1
        else:
            if ord(i)>64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                consoment += 1
    return '单词个数%d,元音个数%d,辅音个数%d' % (chrNum, vowelNum, consoment)
if __name__ == '__main__':
    string = input('请输入一段字符串：')
    print(countChr(string))
