#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:44:06 2020

@author: feel-liao
"""
#读取文件的方式，当读取大文件时，只能用循环输出的方式避免内存溢出

file_name="demo.txt"
with open(file_name) as  file_obj:
    read_lenth=200
    while True:
        text=file_obj.read(read_lenth)
        if not text:
            break
        print(text,end="")
#write可以向文件中写入字符串，但是会覆盖原文件
"""   
with open(file_name,"w") as  file_obj:
    r=file_name.write("aaa")
    print(r)
如果不希望源文件被覆盖 file_obj=open(file_name,"a") 用a表示添加
file_obj=open(file_name,"a")
r=file_obj.write("aaa")
#s=file_obj.read()
file_obj=open(file_name,"r")
print(file_obj.read())
"""


    

        

