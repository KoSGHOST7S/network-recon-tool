#!/usr/bin/python3

import dns.resolver
import dns.reversename

# create DNS resolver thattt takes an IP and tells us what resolves
forwardDNS = dns.resolver.Resolver()
forwardDNS.nameservers = ['192.168.1.10']

#list hostnames to lookup
names = ['ns.mininet.net','mail.mininet.net','www.mininet.net','db.mininet.net','store.mininet.net']

# loop through all hostnames and resolve them for IPs
print("A record lookups include:")
for name in names:
	ans = forwardDNS.resolve(name,"A")
	print (f"{name}->{ans[0]}")

print()
# reverse lookups given an IP find the hostname
reverseDNS = dns.reversename

ips = ['192.168.1.10','192.168.1.11','192.168.1.12','192.168.1.13','192.168.1.14']

print("PTR record lookups include:")
for ip in ips:
	ptr = reverseDNS.from_address(ip)
	ans = forwardDNS.resolve(ptr,"PTR")
	print (ans[0])

