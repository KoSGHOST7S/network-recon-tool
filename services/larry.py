#!/usr/bin/python3

from socket import * 
import requests
import urllib.request
import hashlib

def httpcheck(tgthost):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgthost, 80)
		connSkt.close()
		
		url = 'http://' + tgthost
		response = requests.get(url)
		print(response.text)
	except:
		print('no connection')

