
from django import Django,redirect


import mysql.connector

mydb=mysql.connector.connect(
    host="ocalhost"
    database="dbs_project"
)
mycursor=mydb.cursor()
def login(request):
    if request.method=="POST" :
        userName=request.POST.get("userName").strip.lower()
        password=request.POST.get("password")
        try:
            checkUserId = mycursor.execute("Select userId from registered_users r where r.userId=? and r.password=?",(getUserId(),getPassword))
            if checkUserId !=0:
                return redirect("{% '#'  %} ")
            raise Exception()
        except:
            messages.add_message(request, messages.INFO,"You have supplied invalid login credentials, please try again!", "danger")
            return redirect("{% '#'  %} ")
    return render(request,"login.html")




