#!usr/bin/env python

#Import modules for CGI handling
import cgi,cgitb
#Create instance of FieldStorage
fields=cgi.FieldStorage()
# cgitb.enable()




#Get data from fields
first_name=fields.getvalue('first_name')
last_name=fields.getvalue('last_name')
 
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello-SecondCGIProgram</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>"%(first_name,last_name))
print("</body>")
print("</html>")