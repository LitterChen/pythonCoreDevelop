#!usr/bin/env python3
# -*- coding:utf-8 -*-

def multx(x):
	try:
		return x**2    #运算符不适用字符串，需要自己进行字符串转换
	except TypeError:
		try: 
			return int(x)**2
		except ValueError:
			try:
				return float(x)**2
			except ValueError:
				print('请输入数字')
if __name__ == '__main__':
	x = input('输入一个数字')
	if multx(x) :
		print(multx(x))
