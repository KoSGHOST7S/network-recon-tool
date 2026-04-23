#!/usr/bin/python3

import dns.resolver #import the module
import dns.reversename
import poplib
from socket import *
from sys import argv


# Modified dnsCheck routine...
def dnsCheck(tgtHost):
   dnsHost = '10.0.95.80'
   try:
      forwardDNS = dns.resolver.Resolver()
      forwardDNS.nameservers = [ dnsHost ]
      ans = forwardDNS.query(tgtHost, "A")
      print(tgtHost, ans[0])
      return(str(ans[0]))

   except:
      print('No connection...')
      return(None)


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
    print(tgtHost)


def main():
   if len(argv) == 2:
      script, tgthost = argv
      ip = dnsCheck(tgthost)
      if ip is not None:
         POPCheck(ip)
   else:
      print('./sampleCheck.py host')
 
if __name__ == "__main__":
   main()

