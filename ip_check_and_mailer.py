#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib,urllib,time
from email.mime.text import MIMEText

def ipcheck():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(" yourmail  @gmail.com","password")
	ip = urllib.URLopener().open("http://echoip.com/").readline()
	if ip in open('ip.txt','a+').read():
		mail = "IP adress still the same and %s " % ip
	else:
		mail = "New IP adress is %s " % ip
		open('ip.txt','w').write(ip)
	msg = MIMEText(mail)
	msg["Subject"] = "Server IP Adress"
	msg["From"] = " yourmail  @gmail.com"
	msg["To"] = " Sendto  @gmail.com"
	server.sendmail(" yourmail  @gmail.com", [" Sendto  @gmail.com"], msg.as_string())
	server.quit()
	
while True:
	ipcheck()
	time.sleep(7200)
