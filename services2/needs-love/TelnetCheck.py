#!/usr/bin/python3

from sys import argv
from socket import *
import telnetlib

def connScan(tgtHost):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    print('hello')
    connSkt.settimeout(2)
    connSkt.connect((tgtHost, 23))
    connSkt.close()
    print('hello')
    tn = telnetlib.Telnet(tgtHost)
    tn.read_until(b"login: ",2)
    tn.write(b"admin\n")
    tn.read_until(b"assword: ",2)
    tn.write(b"admin\n")
    tn.write(b"exit\n")
    log = tn.read_until(b"logout", 2).decode('ascii')
    if 'logout' in log:
        print('Telnet exists')
    else:
        print('No connection...')
  except:
    print('No connection...')
  finally:
    connSkt.close()

def main():
  script, ip = argv
  connScan(ip)

if __name__ == "__main__":
  main()
