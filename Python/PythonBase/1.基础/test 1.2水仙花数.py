#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:01:07 2020

@author: feel-liao
"""
i=100
while i<1000:
    a=int(i/100)
    b=int(i/10%10)
    c=int(i%10)
    if a**3+b**3+c**3==i:
        print(i)
    i+=1

