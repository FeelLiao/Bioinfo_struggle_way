# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("求n以内的所有质数")
n=int(input("Please input a num:"))
i=2
while i<=10000:
    flag=True
    j=2
    while j<i:
        if i%j==0:
            flag=False
        j+=1
    if flag:
       print(i)
    i+=1

