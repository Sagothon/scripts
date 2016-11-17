#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="sample")        # name of the data base

cur = db.cursor()

cur.execute("select * from customers")

for row in cur.fetchall():
	print row

db.close()