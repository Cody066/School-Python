#usr/local/bin/python3

# sudo /usr/local/bin/python3 -m pip install pymysql
# brew install mysql
# brew tap homebrew/services
# brew services start mysql  
# pip3 install mysqlclient
# mysql -uroot
# mysql> CREATE DATABASE assignment3;
# mysql> use assignment3;

import pymysql

db = pymysql.connect('localhost', 'root',"","assignment3")

cursor = db.cursor()

"""
CREATE TABLE registered_users(
   PersonID int NOT NULL AUTO_INCREMENT,
   Title varchar(255),
   FirstName varchar(255),
   LastName varchar(255),
   Street varchar(255),
   City varchar(255),
   Province varchar(255),
   PostalCode varchar(255),
   Country varchar(255),
   Phone varchar(255),
   Email varchar(255),
   Sub BOOLEAN,
   PRIMARY KEY (PersonID)
  );
"""


import cgi 
from wsgiref.simple_server import make_server


html = """
<!DOCTYPE html>    
<html>
    <head>
        <title>Assignment 3</title>
    </head>
    <body>
        <FORM action = '' method = 'post'>
        <label for ='title'>Title</label>
            <select name = 'title'>
                <option value=""></option>
                <option value="Mr">Mr</option>
                <option value="Mrs">Mrs</option>
                <option value="Ms">Ms</option>
                <option value="Dr">Dr</option>
            </select>
            </br>
            <label for ='firstName' >First Name</label>
            <input type = 'text' name = 'firstName' value = ''/>
            </br>
            <label for ='lastName'>Last Name</label>
            <input type = 'text' name = 'lastName' value = ''/>
            </br>
            <label for ='street'>Street</label>
            <input type = 'text' name = 'street' value = ''/>
            </br>
            <label for ='city'>City</label>
            <input type = 'text' name = 'city' value = ''/>
            </br>
            <label for ='province'>Province</label>
            <input type = 'text' name = 'province' value = ''/>
            </br>
            <label for ='postalCode'>Postal Code</label>
            <input type = 'text' name = 'postalCode' value = ''/>
            </br>
            <label for ='country'>Country</label>
            <select name = 'country'>
                <option value=""></option>
                <option value="Canada">Canada</option>
                <option value="USA">USA</option>
            </select>
            </br>
            <label for ='phone'>Phone</label>
            <input type = 'text' name = 'phone' value = ''/>
            </br>
            <label for ='email'>Email</label>
            <input type = 'text' name = 'email' value = ''/>
            </br>
            <label for ='sub'>Newsletter Sub</label>
            <input type = 'checkbox' name = 'sub' value = ''/>
            </br>
            <input type  ='submit' name = 'submit' value = 'submit'/>

        </FORM>
    </body>
</html>        
    """





def app(environ, start_reponse):
    response = html

    table = """<table>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Street</th>
                    <th>City</th>
                    <th>Province</th>
                    <th>Postal Code</th>
                    <th>Country</th>
                    <th>Phone</th>
                    <th>Email</th>
                    <th>Subscription</th>
                </tr>
                <tr>    
                    """

    errors = 0

    if (environ['REQUEST_METHOD'] == 'POST'):
        #response = "<B>You submitted the form </B>"
        post_env = environ.copy()
        post = cgi.FieldStorage(
            fp = environ['wsgi.input'],
            environ= post_env,
            keep_blank_values= True
        )

        title = post['title'].value
        if (title == ""):
            errors += 1
            titleErr = "<font color = 'red'>* Required</font>"
        else : 
            
            titleErr =""

        lastName = post['lastName'].value
        if (lastName == ""):
            errors += 1
            lastNameErr = "<font color = 'red'>* Required</font>"
        else : 
            
            lastNameErr =""

        firstName = post['firstName'].value
        if (firstName == ""):
            errors += 1
            firstNameErr = "<font color = 'red'>* Required</font>"
        else : 
            
            firstNameErr =""

        street = post['street'].value
        if (street == ""):
           errors += 1
           streetErr = "<font color = 'red'>* Required</font>"
        else : 
            
            streetErr =""

        city = post['city'].value
        if (city == ""):
            errors += 1
            cityErr = "<font color = 'red'>* Required</font>"
        else : 
            
            cityErr =""

        province = post['province'].value
        if (province == ""):
            errors += 1
            provinceErr = "<font color = 'red'>* Required</font>"
        else :
             errors += 0
             provinceErr =""

        postalcode = post['postalCode'].value
        if (postalcode == ""):
            errors += 1
            postalcodeErr = "<font color = 'red'>* Required</font>"
        else : 
            
            postalcodeErr =""

        country = post['country'].value
        if (country == ""):
            errors += 1
            countryErr = "<font color = 'red'>* Required</font>"
        else : 
            
            countryErr =""

        phone = post['phone'].value
        if (phone == ""):
            errors += 1
            phoneErr = "<font color = 'red'>* Required</font>"
        else : 
            
            phoneErr =""

        email = post['email'].value
        if (email == ""):
            errors += 1
            emailErr = "<font color = 'red'>* Required</font>"
        else : 
            
            emailErr =""

        sub = post['sub'].value
        if (sub == ""):
            sub = 0
        else :
            sub = 1
        
        
            
        
        if (errors == 0):
            sql = """INSERT INTO registered_users (Title,LastName,FirstName,Street,City,Province,PostalCode,Country,Phone,Email,Sub) 
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"""

            values = [title ,lastName, firstName, street,city,province,postalcode,country,phone,email,sub]

            cursor.execute(sql, values)
            db.commit()
            #cursor.close()

            sql = """SELECT * FROM registered_users"""

            cursor.execute(sql)
            data = cursor.fetchall()

            
                            

            for row in data :
                id = row[0]
                title = row[1]
                lastname = row[2]
                firstname = row[3]
                street = row[4]
                city = row[5]
                province = row[6]
                postalcode = row[7]
                country = row[8]
                phone = row[9]
                email = row[10]
                sub = row[11]


                table += """<td>"""
                table += str(id)
                table += """</td>"""

                table += """<td>"""
                table += title
                table += """</td>"""  

                table += """<td>"""
                table += lastname
                table += """</td>""" 

                table += """<td>"""
                table += firstname
                table += """</td>""" 

                table += """<td>"""
                table += street
                table += """</td>""" 

                table += """<td>"""
                table += city
                table += """</td>""" 

                table += """<td>"""
                table += province
                table += """</td>""" 

                table += """<td>"""
                table += postalcode
                table += """</td>""" 

                table += """<td>"""
                table += country
                table += """</td>""" 

                table += """<td>"""
                table += phone
                table += """</td>"""    

                table += """<td>"""
                table += email
                table += """</td>"""  

                table += """<td>"""
                table += str(sub)
                table += """</td>""" 

                table += """</tr>"""

            response = table


    if (errors != 0):
            htmlErr = """<!DOCTYPE html>    
                    <html>
                        <head>
                            <title>Assignment 3</title>
                        </head>
                        <body>
                            <FORM action = '' method = 'post'>
                            <label for ='title'>Title</label>
                                <select name = 'title'>
                                    <option value="%s"></option>
                                    <option value="Mr">Mr</option>
                                    <option value="Mrs">Mrs</option>
                                    <option value="Ms">Ms</option>
                                    <option value="Dr">Dr</option>
                                </select>
                                %s
                                </br>
                                <label for ='firstName' >First Name</label>
                                <input type = 'text' name = 'firstName' value = '%s'/>
                                %s
                                </br>
                                <label for ='lastName'>Last Name</label>
                                <input type = 'text' name = 'lastName' value = '%s'/>
                                %s
                                </br>
                                <label for ='street'>Street</label>
                                <input type = 'text' name = 'street' value = '%s'/>
                                %s
                                </br>
                                <label for ='city'>City</label>
                                <input type = 'text' name = 'city' value = '%s'/>
                                %s
                                </br>
                                <label for ='province'>Province</label>
                                <input type = 'text' name = 'province' value = '%s'/>
                                %s
                                </br>
                                <label for ='postalCode'>Postal Code</label>
                                <input type = 'text' name = 'postalCode' value = '%s'/>
                                %s
                                </br>
                                <label for ='country'>Country</label>
                                <select name = 'country'>
                                    <option value="%s"></option>
                                    <option value="Canada">Canada</option>
                                    <option value="USA">USA</option>
                                </select>
                                %s
                                </br>
                                <label for ='phone'>Phone</label>
                                <input type = 'text' name = 'phone' value = '%s'/>
                                %s
                                </br>
                                <label for ='email'>Email</label>
                                <input type = 'text' name = 'email' value = '%s'/>
                                %s
                                </br>
                                <label for ='sub'>Newsletter Sub</label>
                                <input type = 'checkbox' name = 'sub' value = ""/>
                                </br>
                                <input type  ='submit' name = 'submit' value = 'submit'/>

                            </FORM>
                        </body>
                    </html> """ %(title,titleErr,firstName,firstNameErr,lastName,lastNameErr,street,streetErr,city,cityErr,province,provinceErr,postalcode,postalcodeErr,country,countryErr,phone,phoneErr,email,emailErr)

            response = htmlErr

    start_reponse('200 OK', [('Content-Type','text/html')])
    return [response.encode()]

if __name__ =='__main__':
    try:
        httpd = make_server('', 8080, app)
        print('Serving on port 8080')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye')


cursor.close()
db.close()