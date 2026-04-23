#!/usr/bin/python3

from sys import argv
from socket import *
import paramiko 

def SSHCheck(tgtHost):
   try:
      connSkt = socket(AF_INET, SOCK_STREAM)
      connSkt.settimeout(5.0)
      connSkt.connect((tgtHost, 22))
      connSkt.close()
      # Log output from SSH Client
      # paramiko.util.log_to_file('paramiko.log')
      ssh = paramiko.SSHClient()
      ssh.load_system_host_keys()
      ssh.connect(tgtHost, 22, 'admin', 'admin')
      # Execute a command
      # stdin, stdout, stderr = ssh.exec_command('ls')
      ssh.close()
      print('SSH exists')
   except:
      print('No connection...')
   finally:
      connSkt.close()

def main():
   if len(argv) == 2:
      script, ip = argv
      SSHCheck(ip)
   else:
      print('./SSHCheck.py ssh-server-ip')
 
if __name__ == "__main__":
   main()
