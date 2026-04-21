#!/usr/bin/python3

import dns.resolver
import dns.reversename

# create DNS resolver thattt takes an IP and tells us what resolves
forwardDNS = dns.resolver.Resolver()
forwardDNS.nameservers = ['192.168.1.10']

#list hostnames to lookup
names = ['ns.mininet.net','mail.mininet.net','www.mininet.net','db.mininet.net','store.mininet.net']

# loop through all hostnames and resolve them for IPs
for name in names:
	ans = forwardDNS.query(name,"A")
	print (f"{name}->{ans[0]}")

