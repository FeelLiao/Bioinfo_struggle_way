#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:30:44 2020

@author: feel-liao
"""
print("-"*20,"欢迎使用员工管理系统","-"*20) #显示欢迎信息
emps=["李小涛\t18\t男\t北京"]
while True:
    print("请选择要进行的操作：")
    print("\t 1.查询员工")
    print("\t 2.添加员工")
    print("\t 3.删除员工")
    print("\t 4.退出系统")
    #显示用户选项
    user_choose=int(input('请选择[1-4]:'))
    print("-"*62)
    if user_choose==1:
        n=1
        print("\t序号\t姓名\t年龄\t性别\t住址")
        for emp in emps:
            print(f"\t{n}\t{emp}")
            n+=1
    elif user_choose==2:
        emp_name=input("请输入员工姓名")
        emp_age=input("请输入员工年龄")
        emp_gender=input("请输入员工性别")
        emp_address=input("请输入员工地址")
        emp=f"{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}"
        print("以下员工将被添加到系统中")
        print("-"*62)
        print("\t姓名\t年龄\t性别\t住址")
        print("\t",emp)
        print("-"*62)
        user_confirm=input("是否确认该操作[Y/N]:")
        if user_confirm =="y":
            emps.append(f"{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}")
            print("添加成功")
        else:
            print("取消成功")       
    elif user_choose==3:
        del_num=int(input("请输入要删除员工的序号："))
        if del_num>len(emps):
            print("输入的序号非法")
        else:
            del_i=del_num-1
            print("以下员工将被删除：")
            print("-"*62)
            print("\t姓名\t年龄\t性别\t住址")
            print(f"\t{del_num}\t{emps[del_i]}")
            print("-"*62)
            user_confirm=input("是否确认该操作[Y/N]:")
            if user_confirm =="y":
                emps.pop(del_i)
                print("员工已被删除！")
            else:
                print("操作取消！")
    elif user_choose==4:
        print("你已经成功退出系统！")
        input("请按回车健退出!")
        break
    else:
        print("你的输入有误，请重新输入！")
    print("-"*62)
    
    






