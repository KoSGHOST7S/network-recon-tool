#!/usr/bin/python3

from sys import argv
from socket import *
from smtplib import SMTP

def SMTPCheck(tgtHost):
   try:
      connSkt = socket(AF_INET, SOCK_STREAM)
      connSkt.settimeout(5)
      connSkt.connect((tgtHost, 25))
      connSkt.close()
      smtp = SMTP(tgtHost)
      smtp.quit()
      print('SMTP OK')
   except:
      print('No connection...')

def main():
   if len(argv) == 2:
      script, ip = argv
      SMTPCheck(ip)
   else:
      print('./SMTPCheck.py smtp-server-ip')

if __name__ == "__main__":
   main()

