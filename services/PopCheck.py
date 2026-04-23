#!/usr/bin/python

from sys import argv
from socket import *
import poplib

def PopCheck(tgtHost):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.connect((tgtHost, 110))
    connSkt.close()
    pop3 = poplib.POP3(tgtHost)
    pop3.user('admin')
    pop3.pass_('admin')
    numMessages = len(pop3.list()[1])
    print('Pop3 exists: ' + str(numMessages))
  except:
    print 'No connection...'
  finally:
    connSkt.close()

def main():
  script, ip = argv
  PopCheck(ip)

if __name__ == "__main__":
  main()
