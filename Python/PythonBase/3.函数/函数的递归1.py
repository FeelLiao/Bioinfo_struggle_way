#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:17:04 2020

@author: feel-liao
"""
#  这是一个求一个数几次幂的示例
num=int(input("Please input a num:"))
mum=int(input("Please input a num:"))
def power(n,m):
    if m==0:
        return 1
    result=n*power(n,(m-1))
    return result
a=power(num,mum)
print(a)


    
    

