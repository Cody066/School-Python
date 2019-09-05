#!/usr/local/bin/python3

# mysql> CREATE DATABASE testpython;
# mysql> use testpython;


import pymysql
import gc

db = pymysql.connect('localhost', 'root',"","testpython", cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

sql = """SELECT * FROM TestPerson"""

cursor.execute(sql)
data =  cursor.fetchall()

for row in data :
    id = row["PersonID"]
    lastname = row["LastName"]
    firstname = row["FirstName"]
    address = row["Address"]
    city = row["City"]

    print(str(id) + " / " + firstname + " " + lastname + " / " + address + " / " + city)






cursor.close()
db.close()


gc.collect()