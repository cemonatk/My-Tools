#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib,urllib,time
from email.mime.text import MIMEText

def ipcheck():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(" yourmail  @gmail.com","password")
	addr = urllib.URLopener()
	response = addr.open("http://echoip.com/")
	ip = response.readline()
	if ip in open('ip.txt','a+').read():
		mail = "IP adress still the same and %s " % ip
	else:
		mail = "New IP adress is %s " % ip
		f = open('ip.txt','w')
		f.write(ip)
		f.close()
	msg = MIMEText(mail)
	msg["Subject"] = "Server IP Adress"
	msg["From"] = " yourmail  @gmail.com"
	msg["To"] = " Sendto  @gmail.com"
	server.sendmail(" yourmail  @gmail.com", [" Sendto  @gmail.com"], msg.as_string())
	server.quit()
	
while True:
	ipcheck()
	time.sleep(7200)