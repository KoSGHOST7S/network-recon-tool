#!/usr/bin/python3

import subprocess
from sys import argv

def multipingCheck(ips):
   for ip in ips:
      try:
         output = subprocess.Popen(["ping", "-c 1", ip ], 
                     stdout = subprocess.PIPE).communicate()[0]
         if ('Unreachable' in str(output)):
            print(ip, 'is Offline')
         else:
            print(ip, 'is Online')
      except:
         print('Ping Error')

def main():
   iplist = [ '10.0.95.80', '10.0.95.81', '10.0.95.82', 
              '10.0.95.83', '10.0.95.84' ]
   if len(argv) == 1:
      multipingCheck(iplist)
   else:
      print('./multipingCheck')
 
if __name__ == "__main__":
   main()

