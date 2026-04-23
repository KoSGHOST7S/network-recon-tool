#!/usr/bin/python3

from sys import argv
from socket import *
import imaplib

def IMAPCheck(tgtHost):
   try:
      connSkt = socket(AF_INET, SOCK_STREAM)
      connSkt.settimeout(5)
      connSkt.connect((tgtHost, 143))
      connSkt.close()
      imap = imaplib.IMAP4(tgtHost)
      imap.login('admin', 'admin')
      folders = imap.select('INBOX')
      print('IMAP exists: ' + str(folders[1][0]))
   except:
      print('No connection...')
   finally:
      connSkt.close()

def main():
   if len(argv) == 2:
      script, ip = argv
      IMAPCheck(ip)
   else:
      print('./IMAPCheck imap-system-ip')

if __name__ == "__main__":
   main()
