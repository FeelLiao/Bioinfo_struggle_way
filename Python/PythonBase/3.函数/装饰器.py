#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:08:54 2020

@author: feel-liao
"""
#这是一个装饰器练习
def add(a,b):
    c=a+b
    return c
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
#编写装饰器代码，需要另外设置装饰器函数
def begin(old):#这是一个装饰器函数
    #此处的old是一个对象，函数可以传递对象
    def newfn(*ars,**kwars):
        print("begin:")
        result=old(*ars,**kwars)
        #此处的old是一个对象，以对象的形式来传递函数
        print("end")
        return result
    return newfn
result=begin(power)
r=result(2,4)
print(r)

    

