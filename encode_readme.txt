python 内使用 unicode 码表，所以编码方式默认是 utf-8
如果需要使用gbk或者其他编码，则在读取或者写入的io的时候:
	需要encode二进制位string，或者decode string 为 二进制
	机器内部的存储和传输是二进制的
        所以注意和io相关打交道的地方要指定编码,如果指定编码还是有问题，就尝试手动encode

# coding: utf-8 如果这个出现在python脚本的顶部，代表了python脚本文本内部的编码方式

一个文件如果使用了 utf-8和gbk两种方式写入；使用open(f,ecoding='gbk')
可以使用file.seek(number)跳过一定的字符数，然后使用file.read()
读取余下部分内容
