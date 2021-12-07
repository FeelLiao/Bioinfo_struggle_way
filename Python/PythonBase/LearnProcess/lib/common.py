#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:38:50 2020

@author: feel-liao
"""
#指定列表的所有元素小写
def Lower_words(L1):
    for i in L1:
        if isinstance(i,int) or i==None:
            L1.pop(L1.index(i))
    a=[s.lower() for s in L1]
    return a
#输出杨辉三角形
def Traiangles(stop_n):
    def triangles():
        tri=[1]
        while True:
            yield tri
            tri.append(0)
            tri=[tri[i-1]+tri[i] for i in range (len(tri))]
    n=0
    for t in triangles():
        print(t)
        n=n+1
        if n==stop_n:
            break
#返回几个数的连乘
from functools import reduce
def prod(L):
    def mul(n1,n2):
        return n1*n2
    r=reduce(mul,L)
    return r
#输出指定范围内的素数
def PrimeNumber(stop_n):
    def _odd_iter():
        n=1
        while True:
            n=n+2
            yield n
    def _not_divisible(n):
        return lambda x:x%n>0
    def primes():
        yield 2
        it=_odd_iter()
        while True:
            n=next(it)
            yield n
            it=filter(_not_divisible(n),it)
    for n in primes():
        if n<stop_n:
            print(n)
        else:
            break
# 无参数装饰器
def auther(func): # auther 无参数认证装饰器
    def inner(*args,**kwargs):
        uname=input("请输入你的用户名>>")
        pwd=input("请输入你的密码>>")
        if uname=="feel" and pwd=="123" :
            res=func(*args,**kwargs)
            return res
        else:
            print("login failed, please check out your username and pwd")
    return inner

# auther 有参数装饰器
def auther(db_type): #auther 有参数认证装饰器 db_type:认证类型
    def auth(func):
        def inner(*args,**kwargs):
            uname=input("please input your username>>").strip()
            pwd=input("please input your password>>").strip()
            if db_type=="file":
                if uname == "feel" and pwd == "123":
                    print("authentication based on file")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("login valid")
            elif db_type=="sql":
                if uname == "feel" and pwd == "123":
                    print("authentication based on sql")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("login valid")
            elif db_type=="ladp":
                if uname == "feel" and pwd == "123":
                    print("authentication based on ladp")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("login valid")
            else:
                    print("unknown type of data")
        return inner
    return auth
# 二分法查找已排序列表中的定值
def denary_find(lst,find_num):
    print(lst)
    if len(lst)==0:
        print("the value is not the list")
        return
    mid_index = len(lst) // 2
    if find_num>lst[mid_index]:
        lst=lst[mid_index+1:]
        denary_find(lst,find_num)
    elif find_num<lst[mid_index]:
        lst=lst[:mid_index]
        denary_find(lst,find_num)
    else:
        print("find it")
        print(lst[mid_index])
# 进度条
# 需要提前计算好下载大小和总大小的比值作为参数传入，并且循环调用此函数
def progress(percent):
    if percent>1:
        percent=1
    res=int(50*percent)*"#"
    print("\r[%-50s] %d%%" %(res,int(100*percent)),end="")
# 随机验证码的生成
import random
def RandomVerificationCode(lenth):
    n = 0
    Code = ""
    while n < lenth:
        random_num = str(random.randint(1, 9))
        random_chr = chr(random.randint(65, 90))
        Code += random.choice([random_num, random_chr])
        n += 1
    return Code
# 使用hash sha256 加密
import hashlib
def hash_encipher(o):
    def encipher(o_typed):
        encipher_machine = hashlib.sha256(o_typed)
        res = encipher_machine.hexdigest()
        return res
    if str(type(o)) == "<class 'bytes'>":
       res=encipher(o)
    else:
       o_typing = o.encode("utf-8")
       res=encipher(o_typing)
    return res











