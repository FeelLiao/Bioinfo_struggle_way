#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:18:32 2020

@author: feel-liao
"""
import openpyxl
from openpyxl.chart import (
    Reference,
    Series,
    PieChart,
    BarChart,
    BubbleChart
    )
wb=openpyxl.Workbook()
# Pie Chart
data=[
      ["Pie",'Sold']
      ["Apple",50]
      ["Cherry",30]
      ["Pumpkin",10]
      ["Chocolate",40]
      ]
pie_chart=wb.active
pie_chart.title='PieChart'
# write data to the PieChart
for row in data:
    pie_chart.append(row)
pie=PieChart()
labels=Reference(pie_chart,min_col=1,min_row=2,max_row=5)
data=Reference(pie_chart,min_col=2,min_row=2,max_row=5)
pie.add_data(data)

