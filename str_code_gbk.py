#!/bin/env python3
# coding: gbk

str = '测试gbk的情况'
f = open('./code_file','a',encoding='gbk')
f.write(str)
f.close()
