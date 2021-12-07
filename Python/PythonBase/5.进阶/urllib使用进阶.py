#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:26:22 2020

@author: feel-liao
"""
"""
urllib的使用，配置用户代理详见网络爬虫.py
from urllib.request import urlopen
from http.client import HTTPResponse
url="http://www.bing.com"
response=urlopen(url)
print(response.closed)
with response:
    print(type(response))
    print(response._method)
    print(response.read())
    print(response.status)
    print(response.geturl())
print(response.closed)
用户代理
ua_file="网络爬虫.py"
with open(ua_file) as file_obj:
    read_lenth=200
    while True:
        text=file_obj.read(read_lenth)
        if not text:
            break
        print(text,end="")
"""
#url的编码和解码
'''
from urllib import parse
encode_info={"q":"中国"}
url_encoding=parse.urlencode(encode_info) #编码
url="https://www.bing.com/search?{}".format(url_encoding) #format为格式化字符串的函数
print(url)
print("中".encode("utf-8"))
print(parse.unquote(url_encoding))#解码
'''

