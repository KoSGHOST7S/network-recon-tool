#!/usr/bin/python

import hashlib
from sys import argv
from socket import *

def connScan(tgtHost):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.connect((tgtHost, 80))
    connSkt.send(b'GET / HTTP/1.1\r\n')
    results = connSkt.recv(4096)
    myHash = hashlib.md5()
    myHash.update(results)
    print ("URL: " + tgtHost + ", Hash: " + myHash.hexdigest())
  except:
    print ('No connection...')
  finally:
    connSkt.close()

def main():
  script, ip = argv
  connScan(ip)

if __name__ == "__main__":
  main()
