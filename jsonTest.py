#!/usr/local/bin/python3


import json

json_students = """
{
    "students":[
        {
            "first_name" : "me1",
            "last_name" : "me2"
        },    
        {
            "first_name" : "you1",
            "last_name" : "you2"
        }
    ],
    "teachers":[
        {
            "first_name" : "bert",
            "last_name" : "bert"
        },    
        {
            "first_name" : "ern",
            "last_name" : "ern"
        }
    ]
}



"""


decoded_students = json.loads(json_students)

for student in decoded_students["students"]:
    print("First name : %s" % student["first_name"])
    print("Last name : %s" % student["last_name"])