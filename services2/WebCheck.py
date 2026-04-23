#!/usr/bin/python3

import hashlib
from sys import argv
from socket import *

def WebCheck(tgtHost):
   try:
      connSkt = socket(AF_INET, SOCK_STREAM)
      connSkt.settimeout(5)
      connSkt.connect((tgtHost, 80))
      connSkt.send(b'GET /\r\n')
      results = connSkt.recv(4096)
      myHash = hashlib.md5()
      myHash.update(results)
      print("URL: ", tgtHost, ", Hash: ", myHash.hexdigest())
   except:
      print('No connection...')
   finally:
      connSkt.close()

def main():
   if len(argv) == 2:
      script, ip = argv
      WebCheck(ip)
   else:
      print('./WebCheck.py http-server-ip')

if __name__ == "__main__":
   main()
