#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:19:26 2020

@author: feel-liao
"""
import math
#这是一个封装的示例
class Rectangle:
#利用改变属性名称的方法来实现隐藏属性的目地
#并且利用get_属性名的方法来实现对属性的读取，set_属性实现对属性的写入
    def __init__(self,width,height):
        self.hidden_width=width
        self.hidden_height=height
    def get_width(self):
        return self.hidden_width
    def get_height(self):
        return self.hidden_height
    def set_width(self,width):
        self.hidden_width=width
    def set_height(self,height):
        self.hidden_height=height
    def get_area(self):
        area=self.hidden_width*self.hidden_height
        return area
Rectangle_1=Rectangle(4,5)
Rectangle_2=Rectangle(6,8)
print(Rectangle_1.get_area())
print(Rectangle_2.get_area())
Rectangle_1.set_width(13)
print(Rectangle_1.get_area())

class Trangle():
#利用__来实现对属性的隐藏
    def __init__(self,lenth_1,lenth_2,lenth_3):
        self.__lenth_1=lenth_1
        self.__lenth_2=lenth_2
        self.__lenth_3=lenth_3
    def get_lenth_1(self):
       return self.__lenth_1
    def get_lenth_2(self):
        return self.__lenth_2
    def get_lenth_3(self):
        return self.__lenth_3
    def set_lenth_1(self,lenth_1):
        self.__lenth_1=lenth_1
    def set_lenth_2(self,lenth_2):
        self.__lenth_2=lenth_2
    def set_lenth_3(self,lenth_3):
        self.__lenth_3=lenth_3
    def get_area(self):
        lenth=[self.__lenth_1,self.__lenth_2,self.__lenth_3]
        del_num=0
        max_lenth=max(self.__lenth_1,self.__lenth_2,self.__lenth_3)
        for n in lenth:
            if n==max_lenth:
                lenth.pop(del_num)
                break
            del_num+=1
        s=0
        for m in lenth:
            s+=m
        if max_lenth<s :
            lenth_sum=self.__lenth_1+self.__lenth_2+self.__lenth_3
            p=float(lenth_sum/2)
            p1=p-self.__lenth_1
            p2=p-self.__lenth_2
            p3=p-self.__lenth_3
            area=math.sqrt(p*p1*p2*p3)
            return area
        else:
            return "invalid lenth"
Trangle_1=Trangle(3,4,5)
area=Trangle_1.get_area()
print(area)




        
        
    
        
        
        




        

