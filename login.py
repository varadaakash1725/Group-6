userId
password

import mysql.connector

mydb=mysql.connector.connect(
    host="ocalhost"
    database="dbs_project"
)
mycursor=mydb.cursor()

checkUserId = mycursor.execute("Select userId from registered_users r where r.userId=? and r.password=?",(userId,password))

if checkUserId !=0:
    alert()
    
else:
    
    



