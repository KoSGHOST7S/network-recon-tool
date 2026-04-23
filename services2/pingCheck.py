#!/usr/bin/python3

from sys import argv
import subprocess

def pingCheck(ip):
   try:
      output = subprocess.Popen(["ping", "-c 1", "192.168.1.10"], 
                  stdout = subprocess.PIPE).communicate()[0]
   except:
      print('Ping Error')

   if ('Unreachable' in str(output)):
      print('Offline')
   else:
      print('Online')

def main():
   if len(argv) == 2:
      script, ip = argv
      pingCheck(ip)
   else:
      print('./pingCheck target-ip')
 
if __name__ == "__main__":
   main()
