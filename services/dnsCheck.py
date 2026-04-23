#!/usr/bin/python

import dns.resolver #import the module
import dns.reversename

forwardDNS = dns.resolver.Resolver() #create a new instance named 'myResolver'
forwardDNS.nameservers = ['10.0.95.80']
names = ['ns.mininet.local', 'www.mininet.local', 'db.mininet.local', 'mail.mininet.local', 'store.mininet.local']
#lookup = 'www.mininet.local'

for name in names:
     ans = forwardDNS.query(name, "A") #Lookup the 'A' record(s) for www
     print ans[0]

reverseDNS = dns.reversename
reverseDNS.nameservers = ['10.0.95.80']
ips = ['10.0.95.80', '10.0.95.81', '10.0.95.82', '10.0.95.83', '10.0.95.84']

for ip in ips:
     ptr = reverseDNS.from_address(ip)  # Find PTR record for Address
     ans = forwardDNS.query(ptr, "PTR") # Find Name for that PTR
     print ans[0]
