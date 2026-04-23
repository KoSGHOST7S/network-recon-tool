#!/usr/bin/python3

import dns.resolver #import the module
import dns.reversename
from sys import argv

def dnsCheck(tgtHost, tgtName, tgtIP):
   try:
      forwardDNS = dns.resolver.Resolver()
      forwardDNS.nameservers = [ tgtHost ]
      ans = forwardDNS.query(tgtName, "A")
      print(tgtName, ans[0])

      reverseDNS = dns.reversename
      reverseDNS.nameservers = [ tgtHost ]
      ptr = reverseDNS.from_address(tgtIP)  # Find PTR record for Address
      ans = forwardDNS.query(ptr, "PTR") # Find Name for that PTR
      print(tgtName, ans[0])
   except:
      print('No connection...')

def main():
   if len(argv) == 4:
      script, ip, name, ip2 = argv
      dnsCheck(ip, name, ip2)
   else:
      print('Syntax: ./dnsCheck dns-ip dns-name dns-name-ip')
 
if __name__ == "__main__":
   main()
