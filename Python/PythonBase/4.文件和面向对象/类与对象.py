#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:47:37 2020

@author: feel-liao
"""
#这是一个类创建的示例
class People():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def run(self):
        print("I am running")
person=People("Teel",19,"Male")


