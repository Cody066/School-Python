#!/usr/local/bin/python3

# sudo /usr/local/bin/python3 -m pip install pymysql
# brew install mysql
# brew tap homebrew/services
# brew services start mysql  
# pip3 install mysqlclient
# mysql -uroot
# mysql> CREATE DATABASE testpython;
# mysql> use testpython;

"""
CREATE TABLE TestPerson(
   PersonID int NOT NULL AUTO_INCREMENT,
   LastName varchar(255),
   FirstName varchar(255),
   Address varchar(255),
   City varchar(255),
   PRIMARY KEY (PersonID)
  );
"""

"""
INSERT INTO TestPerson (LastName,FirstName,Address,City) 
VALUES ('Me', 'Mine', 'Here', 'There');
"""
"""
SELECT * FROM TestPerson;
"""


import pymysql

db = pymysql.connect('localhost', 'root',"","testpython")

cursor = db.cursor()

#retrieve manual entry from db

cursor.execute("SELECT * FROM TestPerson")
data = cursor.fetchall()

for row in data :
    id = row[0]
    print(str(id))

cursor.close()
db.close()


