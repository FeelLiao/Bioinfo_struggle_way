#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:42:00 2020

@author: feel-liao
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import simplejson
ua='''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
 snap Chromium/80.0.3987.116 Chrome/80.0.3987.116 Safari/537.36'''
jurl="https://movie.douban.com/j/search_subjects?"
d={
   "type":"movie",
   "tag":"热门",
   "page_limit":10,
   "page_start":0,
   }
url="{}?{}".format(jurl,urlencode(d))
req=Request(url,headers={
 "User-agent":ua       
        })
result_file_temp="豆瓣热门电影_temp.txt"
with urlopen(req) as res:
    with open(result_file_temp,"w+") as file_obj_temp: 
        temp=simplejson.loads(res.read())
        result_temp=str(temp)
        file_obj_temp.write(result_temp)
        print(type(file_obj_temp))
        print(len(temp["subjects"]))
        file_obj_temp.close
                

        
        
        
    


