#!/usr/bin/python3

import requests
import urllib.request
import hashlib
url = "http://192.168.1.14"

myHash = hashlib.md5()
response = requests.get(url)
myHash.update(response.text.encode('utf-8'))
print('URL: ' + url + ', Hash = ' + myHash.hexdigest())
