#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:56:13 2020

@author: feel-liao
"""
#open file on local computer
file_local=r"/home/feel-liao//Python/4.文件和面向对象/demo.txt"
with open(file_local) as matching_text:
    matching_list=(matching_text.read())
    alphabet=[chr(i) for i in range(97,123)]
    s=0
    print(matching_list)
    print(alphabet)
    for i in alphabet:
        for c in matching_list:
            if i==c:
                s+=1
        print(i,s)