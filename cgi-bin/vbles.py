#!/usr/bin/python3

import cgi, cgitb

fields = cgi.FieldStorage()

msg=""

for item in fields:
    msg += item + ": " + fields.getvalue(item) + "<br>"

hobby = fields.getvalue('hobby')
first_name = fields.getvalue('first_name')
achter_name = fields.getvalue('achter_name')
tussenvoegsel = fields.getvalue('tussenvoegsel')
vakken = fields.getvalue('vakken')
geslacht = fields.getvalue('Geslacht')
Klas = fields.getvalue('Klas')

print("Content-Type: text/html\n")
print("<html>")
print("<head>")
print("<title>Voorbeeld les</title>")
print("</head>")
print("<body>")
print("<p> %s </p>" % ("Welkom: " +first_name + tussenvoegsel + achter_name + " Leuk dat je " + hobby + " Als hobby hebt."))
print("<p> %s </p>" % ("Voornaam: " +first_name))
print("<p> %s </p>" % ("Achternaam: " +achter_name))
print("<p> %s </p>" % ("Tussenvoegsel: " +tussenvoegsel))
print("<p> %s </p>" % ("Vak: " +vakken))
print("<p> %s </p>" % ("Hobby: " + hobby))
print("<p> %s </p>" % ("Geslacht: " + geslacht))
print("<p> %s </p>" % ("Klas: " + Klas))
#print("<p> %s </p>" % (hobby))

if hobby == vakken:
    print("Super dat je favoriete vak ook je hobby is!")

    
elif hobby != vakken:
    print("Je favoriete vak is niet je hobby begrijp ik. Kunnen we daar iets aan doen?")





print("</body>")
print("</html>")