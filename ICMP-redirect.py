#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__    = '30.04.2016'
__author__  =  'cemonatk'

try:
	from os import system as komut
	from scapy.all import *
	from argparse import ArgumentParser,parse_args
except ImportError,c:
	print c;raise SystemExit(0)
	
