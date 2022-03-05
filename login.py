
from django import Django,request

app=Django(__name__)

@app.route('/',methods=['post'])
def getUserId():
    userId=request.json["userId"]
    return userId
def getPassword():
    password=request.json["password"]
    return password

import mysql.connector

mydb=mysql.connector.connect(
    host="ocalhost"
    database="dbs_project"
)
mycursor=mydb.cursor()

checkUserId = mycursor.execute("Select userId from registered_users r where r.userId=? and r.password=?",(getUserId(),getPassword))

if checkUserId !=0
    



