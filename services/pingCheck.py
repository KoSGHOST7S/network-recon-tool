#!/usr/bin/python3

import subprocess

try:
     output = subprocess.Popen(["ping", "-c 1", "192.168.1.10"], stdout = subprocess.PIPE).communicate()[0]
except:
     print('Ping Error')

if ('Unreachable' in str(output)):
     print('Offline')
else:
	print('Succ')
print(output)
