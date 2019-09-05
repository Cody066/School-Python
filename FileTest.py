#!/usr/local/bin/python3


file =  open('testfile.txt','w')
file.write("Hello World \n")
file.write("Goodbye cruel world\n")
file.close()


#file = open('testfile.txt','w')
#file.write("REEEEEEEEEEEE")
#file.close()

file =  open('testfile.txt','a')
file.write("Hello World 2\n")
file.write("Goodbye cruel world 2")
file.close()

file = open('testfile.txt','r')
myLine = file.readline()
print("My line is: %s" % myLine)
file.close()


file = open('testfile.txt','r')
myLines = file.readlines()

lines = ""

for line in myLines:
    lines += line

print(lines)
file.close