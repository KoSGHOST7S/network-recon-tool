#!/usr/bin/python3

import pymysql
from sys import argv


def mysqlCheck(tgtHost):
   try:
      dbconn = mysql.connect(host=tgtHost, user='admin', password='changeme', database='test', ssl_disabled=True)
      print('Hello',tgtHost)
      dbcur = dbconn.cursor()

      dbcur.execute('select * from test')

      data = dbcur.fetchone()

      # Print all of the records...
      while data:
           print(data)
           data = dbcur.fetchone()
   except:
      print('No connection...')

def main():
   if len(argv) == 2:
      script, ip = argv
      mysqlCheck(ip)
   else:
      print('./mysqlCheck.py mysql-server-ip')

if __name__ == "__main__":
   main()
