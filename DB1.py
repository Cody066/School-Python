#!/usr/local/bin/python3

# mysql> CREATE DATABASE testpython;
# mysql> use testpython;


import pymysql

db = pymysql.connect('localhost', 'root',"","testpython")
cursor = db.cursor()

sql = """INSERT INTO TestPerson (LastName,FirstName,Address,City) 
VALUES (%s, %s, %s, %s)"""

values = ["Me7" , "You7", "Pip7", "911"]

cursor.execute(sql, values)
db.commit()










cursor.close()
db.close()