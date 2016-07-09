#!usr/bin/env python3
# -*- coding:utf-8 -*-

def find2():
	return [i for i in range(20) if not i%2]
def find1():
	return [i for i in range(20) if i%2]
if __name__ == '__main__':
	for j in find2():
		print(j)
	for j in find1():
		print(j)
