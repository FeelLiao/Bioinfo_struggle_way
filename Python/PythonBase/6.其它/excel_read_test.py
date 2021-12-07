#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:24:00 2020

@author: feel-liao
"""
import openpyxl
import matplotlib.pyplot as obj_mat
popwb=openpyxl.load_workbook("/home/feel-liao/Downloads/population.xlsx")
data=popwb.get_sheet_by_name("Data")
TimePopCell=data["E4:BK4"]
TimePop=[]
for cell_row_time in TimePopCell:
    for cell_obj in cell_row_time:
        TimePop.append(cell_obj.value)
ChinaPopCell=data["E43:BK43"]
ChinaPop=[]
for cell_row_pop in ChinaPopCell:
    for cell_obj in cell_row_pop:
        ChinaPop.append(cell_obj.value)
ChinaPopNew=[]
for i in ChinaPop:
    i=i/1000000
    ChinaPopNew.append(i)   
IndiaPopCell=data["E112:BK112"]
IndiaPop=[]
for cell_row_pop in IndiaPopCell:
    for cell_obj in cell_row_pop:
        IndiaPop.append(cell_obj.value)
IndiaPopNew=[]
for i in IndiaPop:
    i=i/1000000
    IndiaPopNew.append(i) 
x=TimePop
y1=ChinaPopNew
y2=IndiaPopNew
obj_mat.figure(figsize=(100,8),dpi=80)
obj_mat.plot(x,y1,color="r",label="China")
obj_mat.plot(x,y2,color="b",label="India")
obj_mat.xticks(x[::5])
obj_mat.grid(True,linestyle="--",alpha=0.5)
font2 = {'family' : 'Times New Roman','weight' : 'normal','size'   : 15,}
obj_mat.legend(loc="lower right")
obj_mat.xlabel("Time",font2)
obj_mat.ylabel("Population million",font2)
obj_mat.show() 










