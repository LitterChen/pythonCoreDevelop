#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
翻译
编写一个rot13翻译器。rot13是个古老又简单的加密算法  就是字母变为当前ascii码之后的13个字母，后半部分映射到前面
再编写一个解密器d_rot13
'''
__author__ = 'Jackie Qiang'
def rot13(str):
    strs = ''
    for i in str:
        num = ord(i)
        if num>64 and num<91:
            if (num+13) % 90 > 20:
                strs += chr(num+13)
            else:
                strs += chr(64+(num+13)%90)
        elif num>96 and num<123:
            if (num+13) % 122 > 20:
                strs += chr(num+13)
            else:
                strs += chr(96+(num+13)%122)
        else:
            strs += i
    return strs
def d_rot13(str):
    strs = ''
    for i in str:
        num = ord(i)
        if num>64 and num<91:
            if (num-13) % 65 < 14:
                strs += chr(num-13)
            else:
                strs += chr(26+(num-13)%65)
        elif num>96 and num<123:
            if (num-13) % 97 < 14:
                strs += chr(num-13)
            else:
                strs += chr(26+(num-13)%98)
        else:
            strs += i
    return strs

if __name__ == '__main__':
    str = input('输入要加密的字符串:')
    print(rot13(str))
    str = input('输入要解密的字符串:')
    print(d_rot13(str))
    
