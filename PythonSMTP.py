#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEBase,MIMEMultipart
from email.header import Header

sender = 'nmliqi@163.com'
password = 'lq910816'
receiver  = 'nmliqi@126.com'
smtpserver = 'smtp.163.com'
smg = MIMEMultipart()
smg.attach(MIMEText('你好，Richie， 这是第一封python邮件','plain','utf-8'))
smg['From'] = sender
smg['To'] = receiver
subject = 'python testing email'
smg['Subject'] = Header(subject,'utf-8')
with open('test.py','rb')as file:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('text','py',filename = 'test.py')
    #添加头文件信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.py')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(file.read())
    smg.attach(mime)

# attach1 = MIMEImage('test.png','png','base64')
# attach1["Content-Type"] = 'application/octet-stream'
# attach1["Content-Disposition"] = 'attachment; filename="test.png"'
# smg.attach(attach1)

server = smtplib.SMTP()
server.connect(smtpserver)
server.login(sender,password)
server.set_debuglevel(1)
server.sendmail(sender,receiver,smg.as_string())
server.quit()

