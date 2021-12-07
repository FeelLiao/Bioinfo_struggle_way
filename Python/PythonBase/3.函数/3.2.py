#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:09:49 2020

@author: feel-liao
"""
b=input("Please input a str:")
def hui_wen(s):
    if len(s)<2:
        return True
    return s[0]==s[-1] and hui_wen(s[1:-1])
a=hui_wen(b)
print(a)



