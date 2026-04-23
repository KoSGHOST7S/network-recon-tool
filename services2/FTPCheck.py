#!/usr/bin/python3

from sys import argv
from socket import *
from ftplib import FTP

def DummyCallBack(data):
   return(data)

def FTPCheck(tgtHost):
   try:
      connSkt = socket(AF_INET, SOCK_STREAM)
      connSkt.settimeout(5)
      connSkt.connect((tgtHost, 21))
      ftp = FTP(tgtHost)
      ftp.login()
      output = ftp.retrlines('LIST', DummyCallBack)
      if ('Directory send OK' in str(output)):
         print('Online')
      else:
         print('Offline')
   except:
      print('No connection...')

def main():
   if len(argv) == 2:
      script, ip = argv
      FTPCheck(ip)
   else:
      print('./FTPCheck.py ftp-server-ip')

if __name__ == "__main__":
   main()

