#!/usr/bin/env python
# -*- coding: utf-8 -*-
__DATE__ = '12.10.2015'
__AUTHOR__ = 'cemonatk'

try:
	import sys,smtplib,urllib,time
	from email.mime.text import MIMEText
except ImportError,module:
	sys.stdout.write("%s" % module)
	raise SystemExit(0)

receiver    = "xxxx@gmail.com"
transmitter = "yourmail@gmail.com"
password    = "yourgmailpassword"

def ipcheck():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(transmitter,password)
	ip = urllib.URLopener().open("http://echoip.com/").readline()
	if ip in open('ip.txt','a+').read():
		#mail = "IP adress is still same and %s " % ip
		pass
	else:
		mail = "New IP adress is %s " % ip
		open('ip.txt','w').write(ip)
	msg = MIMEText(mail)
	msg["Subject"] = "Server IP Adress"
	msg["From"] = transmitter
	msg["To"] = receiver
	server.sendmail(transmitter, [receiver], msg.as_string())
	server.quit()
	
while True:
	ipcheck()
	time.sleep(1800)
