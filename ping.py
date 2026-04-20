#!/usr/bin/python3

import subprocess
# gets IP from user
ip = input("Please enter an IP to ping:")
# opens a subprocess shell to ping and pipes the output to memory.
#If it does not work it prints "something is not working""
try:
    output = subprocess.Popen(
	["ping","-c","1",ip],
	stdout=subprocess.PIPE
	).communicate()[0]
except:
	print("Something went wrong with ping try later")

# if the system is unreachable for some reason, it prints offline
# otherwise if it works dont fix it.
if('Unreachable' in str(output)):
	print('offline')
else:
	print('im guessing something worked')
