#!/usr/bin/python3

import pymysql

dbconn = pymysql.connect('10.0.95.82', 'admin', 'changeme', 'test')
dbcur = dbconn.cursor()

dbcur.execute('select * from test')

data = dbcur.fetchone()

# Print all of the records...
while data:
     print(data)
     data = dbcur.fetchone()
