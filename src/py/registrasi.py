#!C:/Users/Ages/AppData/Local/Programs/Python/Python39/python
import cgi
import mysql.connector
import uuid

print("Content-Type: text/html")
print()
conn = mysql.connector.connect(user='', password='', host='', database='travelday')
curr = conn.cursor()

form =  cgi.FieldStorage()
id = uuid.uuid4()
idStr = str(id)
email = form.getvalue('email')
password = form.getvalue('password')
noTelp = form.getvalue('noTelp')

curr.execute("insert into registrasi_user values(%s, %s, %s, %s)", (idStr, noTelp, email, password))
conn.commit()

curr.close()
conn.close()
print("<meta http-equiv='refresh' content='1;url=http://localhost/projects/TravelDay/TravelDay/index.html'>")
print()  





