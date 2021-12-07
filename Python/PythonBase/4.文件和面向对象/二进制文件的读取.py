#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:56:04 2020

@author: feel-liao
"""
file_old="/home/feel-liao/Music/Different World/Folder.png"
with open(file_old,"rb") as file_old_obj:
    new_file="aa.png"
    with open(new_file,"wb") as file_new_obj:
        chunk=1024*100
        while True:
            content=file_old_obj.read(chunk)
            if not content:
                break
            file_new_obj.write(content)
 
