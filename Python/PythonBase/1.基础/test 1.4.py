#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:55:21 2020

@author: feel-liao
"""
i=0
while i<9:
    i+=1
    j=0
    while j<i:
        j+=1
        print(f"{j}*{i}={i*j} ",end="")
       
    print()
