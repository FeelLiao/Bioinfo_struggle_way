#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:46:08 2020

@author: feel-liao
"""
"""
正则表达式
import re
string=""aliyunedu""
pt="yun\n"
s=re.compile(pt).findall(string)
print(s)
"""
# Urllib爬虫
"""
import urllib
import re
date=urllib.request.urlopen("http://www.jd.com").read().decode("utf-8","ignore")
pat="<title>(.*?)</title>"
a=re.compile(pat,re.S).findall(date)
print(a)
#直接将网页爬到本地磁盘中
urllib.request.urlretrieve("http://www.jd.com",
                           filename =r"/home/feel-liao/Python/5/jd.html")
"""
#伪装浏览器
"""
import urllib
opener=urllib.request.build_opener()
UA=("User-Agent",'''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,
    like Gecko) snap Chromium/80.0.3987.100 Chrome/80.0.3987.100 Safari/537.36''')
opener.addheaders=[UA]
urllib.request.install_opener(opener) #设置全局伪装

"""
#用户代理池，一种破除反爬的策略
#构建用户代理池
"""
import urllib
import random
userpools=['''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,
    like Gecko) snap Chromium/80.0.3987.100 Chrome/80.0.3987.100 Safari/537.36''',
'''User-Agent,Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit
/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50''',
'''User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; 
SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'''
    ]
def UA():
    opener=urllib.request.build_opener()
    true_ua=random.choice(userpools)
    ua=("User-Agent",true_ua)
    opener.addheaders=[ua]
    urllib.request.install_opener(opener)
url="http://www.bing.com"
for i in range(0,10):
    UA()
    date=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    print(len(date))
"""
