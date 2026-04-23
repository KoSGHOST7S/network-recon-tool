#!/usr/bin/python3

from sys import argv
from socket import *
import poplib

def POPCheck(tgtHost):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.settimeout(5)
    connSkt.connect((tgtHost, 110))
    connSkt.close()
    pop3 = poplib.POP3(tgtHost)
    pop3.user('admin')
    pop3.pass_('admin')
    numMessages = len(pop3.list()[1])
    print('Pop3 exists: ' + str(numMessages))
  except:
    print('No connection...')
  finally:
    connSkt.close()

def main():
   if len(argv) == 2:
      script, ip = argv
      POPCheck(ip)
   else:
      print('./POPCheck pop-server-ip')
 
if __name__ == "__main__":
   main()
