#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:24:15 2020

@author: feel-liao
"""

#这是一个发送邮件的测试
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender="feelteel@stu.hunau.edu.cn"
sender_pwd="FliaoHNND5564"
receiver=["m18728023568@163.com"]
message=MIMEText("Python email smtp","plain","utf-8")
message['From']=Header("email test","utf-8")
message['To']=Header("test","utf-8")
subject="python email text"
message["Subject"]=Header(subject,"utf-8")
try:
    smtpObj=smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
    smtpObj.login(sender,sender_pwd)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print("successfully sent")
except smtplib.SMTPException as e:
    print("we meet an error %s" %e)
    """
#发送HTML格式的邮件
# message=MIMEText(mes,"html","utf-8") 其中mes为HTML格式的邮件内容变量

#发送代附件的邮件
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
sender="feelteel@stu.hunau.edu.cn"
sender_pwd="FliaoHNND5564"
receiver=["m18728023568@163.com"]
#创建一个代附件的实例
message=MIMEMultipart()
#邮件正文内容
message.attach(MIMEText("Python email smtp","plain","utf-8"))
#构造附件1
file_name="文件路径"
att1=MIMEText(open(file_name,"rb").read(),"base64","utf-8")
att1["Content-Type"]="application/octet-stream"
att1["Content-Disposition"]="attachment;filename='file-name'"
message.attach(att1)
#发送邮件
message['From']=Header("email test","utf-8")
message['To']=Header("test","utf-8")
subject="python email text"
message["Subject"]=Header(subject,"utf-8")
try:
    smtpObj=smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
    smtpObj.login(sender,sender_pwd)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print("successfully sent")
except smtplib.SMTPException as e:
    print("we meet an error %s" %e)
"""

