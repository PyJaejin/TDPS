# -*- coding: utf-8 -*-
#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders
from email.header import Header
from bs4 import BeautifulSoup
#from urllib.request import urlopen
from urllib2 import urlopen
from RPi import GPIO
import os
import pymysql
import ast



smtp_server = "smtp.gmail.com"
port = 587
portssl = 465
recvid = "trigger@applet.ifttt.com"
db_host = '113.198.236.131'
db_port = 10306
db_user = 'lab919'
db_passwd = 'software'
db_name = 'TSMS'
db_charset = 'utf8mb4'
user_id_list = []
user_passwd_list = []
count = 0
temp = 30

def getUser():
    #user_id = ['hayoung','hyuna']
    db = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_passwd, db=db_name, charset='utf8', autocommit=True)         
    cursor = db.cursor()

# for i in range(len(user_id)):
    sql = "SELECT userid,passwd from user"# where name = '"+str(user_id[i])+"'"
    cursor.execute(sql)
    while True:
        data = cursor.fetchone()
        if data == None: break;
        user_id_list.append(str(data[0]))
        user_passwd_list.append(str(data[1]))
        
    db.close()
    return (user_id_list, user_passwd_list)


def sendmail(user_id, password, cc_users, subject,text,attach):
    COMMASPACE = ", "
    msg = MIMEMultipart("alternative")
    msg["From"] = user_id
    msg["To"] = recvid
    msg["Co"] = COMMASPACE.join(cc_users)
    msg["Subject"] = Header(s=subject, charset="utf-8")
    if(text != None):
        msg.attach(MIMEText(text))
    if(attach != None):
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(attach, "rb").read())
        Encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment",filename=os.path.basename(attach))
        msg.attach(part)
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    ret, m = server.login(user_id, password)
    
    if ret != 235:
        print("login fail")
        return
    
    server.sendmail(user_id,recvid, msg.as_string())
    server.quit()
    
def send_warning_msg(node_id, temp_value, humi_value):
    getUser()
    msg = "place : " + str(node_id) + ", temperature : " + str(temp_value) + ", humidity : " + str(humi_value)
    if temp <= value: 
        for i in range(len(user_id_list)):
            sendmail(user_id_list[i],user_passwd_list[i],"", "warning!!", msg, None)



if __name__ == "__main__":
    print("Hello")
