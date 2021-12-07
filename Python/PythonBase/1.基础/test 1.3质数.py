#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:21:42 2020

@author: feel-liao
"""

num=int(input("Please input a number:"))
i=2
flag=True
while i<num:
    if num%i==0:
        flag=False
        break
    i+=1
if flag:
    print(num,"true")
else:
    print(num,"false")

