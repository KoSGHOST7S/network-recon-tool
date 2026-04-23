#!/usr/bin/python3

import hashlib
import requests
import urllib.request
from sys import argv


def WebCheck(tgtHost):
   try:
      url = 'http://' + tgtHost
      response = requests.get(url)
      myHash = hashlib.md5(response.text.encode())
      print('URL:', url, ' Hash: ', myHash.hexdigest())
   except:
      print('No connection...')


def main():
   if len(argv) == 2:
      script, ip = argv
      WebCheck(ip)
   else:
      print('./WebCheck2.py http-server-ip')

if __name__ == "__main__":
   main()
