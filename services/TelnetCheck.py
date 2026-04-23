#!/usr/bin/python

from sys import argv
from socket import *
import telnetlib

def connScan(tgtHost):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.connect((tgtHost, 23))
    connSkt.close()
    tn = telnetlib.Telnet(tgtHost)
    tn.read_until("login: ",1)
    tn.write('guest\n')
    tn.read_until("assword: ",1)
    tn.write('guest\n')
    tn.write('ls\n')
    tn.write('exit\n')
    print tn.read_until('Closed', 2)
    print 'Telnet exists'
  except:
    print 'No connection...'
  finally:
    connSkt.close()

def main():
  script, ip = argv
  connScan(ip)

if __name__ == "__main__":
  main()
