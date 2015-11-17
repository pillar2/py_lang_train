#!/bin/env python3
from sys import argv
import fileinput
import time

####################read################################
#open 常用配置 mode='r'默认/'w'/'rw'/'a'(append 以追加的方式写)/'b'(二进制的方式)
#         buffering=0无缓冲/>0有缓冲 代表缓冲大小/-1默认缓冲区(默认值)
#         encoding=None默认是系统默认的编码方式

def read4char(file):
	print("read4char")
	f = open(file)
	batch=4
	four_char = f.read(4)
	while four_char:
		print(four_char)
		four_char = f.read(4)
	f.close()	

def read_all1time(file):
	print("read_all1time")
	f = open(file)
	print(f.read())
	f.close()

def read_line1time(file):
	print("read_line1time")
	f = open(file)
	while True: #和 read4char 里的 while 对比下
		line = f.readline()
		if not line:break
		print(line)
	f.close()
	for line in fileinput.input(file):
		print(line)
	

def read_all_lines1time(file):
	print("read_all_lines1time")
	f = open(file)
	for line in f.readlines():
		print(line)
	f.close()

def read_from_some_index(file):
	print("read_from_some_index")
	f = open(file,encoding="utf8")
	f.seek(3)
	print(f.read(4))
	print(f.tell())
	f.close()
# 小结
# read  readlines 慎用 在小文件的时候可用 大文件内存可能不够
# 等同于readline 的 fileinput 也是个选择
# seek 跳过指定的字节数,tell当前所在的字节的索引位置

def tail(file):
	f = open(file)
	while True:
		line = f.readline() 
		if not line:
			time.sleep(2)
			print('hu Hu HU~~')
			continue
		if 'over' in line:break
		yield line

def grep(lines,target_text):
	for line in lines:
		if target_text in line:
			yield line
# yeild 把函数变成生存器 保持函数的内部状态的迭代器

##################write##################################
def write2file(file):
	print("write2file")
	f = open(file,'a')
	try:
		f.write('new line\n')
		f.flush()
	finally:
		f.close()

def write2file_by_with(file):
	print("write2file_by_with")
	with open(file,'a') as ofile:
		ofile.write(" new line by with \n")

def write2file_with_lines(file):
	print("write2file_with_lines")
	lines = ['1\n','2\n','3\n','4\n']
	with open(file,'a') as ofile:
		ofile.writelines(lines)

#读写文件都应该最后都应该close 尤其写文件，
#因为python会换成一部分数据到内存，知道发现close或者flush才同步到硬盘
#with 语法会保证文件的自动关闭，因为file实现了context的方法，在退出上下文的时候回自动关闭文件

if __name__ == '__main__':
	read4char(argv[1])
	read_all1time(argv[1])
	read_line1time(argv[1])
	read_all_lines1time(argv[1])
	read_from_some_index(argv[1])

	
	write2file(argv[1])
	write2file_by_with(argv[1])
	write2file_with_lines(argv[1])

	print('tail & grep ')	
	for line in grep(tail(argv[1]),'hello'):
		print(line)
	
