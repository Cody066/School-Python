#!/usr/local/bin/python3

# mysql> CREATE DATABASE testpython;
# mysql> use testpython;


import pymysql

db = pymysql.connect('localhost', 'root',"","testpython")
cursor = db.cursor()

sql = """SELECT * FROM TestPerson"""

cursor.execute(sql)
data =  cursor.fetchall()

for row in data :
    id = row[0]
    lastname = row[1]
    firstname = row[2]
    address = row[3]
    city = row[4]

    print(str(id) + " / " + firstname + " " + lastname + " / " + address + " / " + city)






cursor.close()
db.close()

import gc
gc.collect()