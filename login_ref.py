import mysql.connector

from tkinter import*
from tkinter import messagebox
from subprocess import call
#def cl():
#    newW.destroy()
def dele():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database = 'sample',
        auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()    
    name=e1.get()    
    sql="DELETE FROM stinfo WHERE Name= %s"
    sq="DELETE FROM login WHERE admin= %s"
    mycursor.execute(sql,[(name)])
    mycursor.execute(sq,[(name)])
    mydb.commit()
    messagebox.showinfo("", "All Record Cleared",)
    #cl()

def Ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="pass", database="sample")
    mycursor = mysqldb.cursor()
    admin= e1.get()
    passw= e2.get()
    
    sql = "select * from login where admin = %s and passw = %s"
    mycursor.execute(sql, [(admin), (passw)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login Success")

        call(["python", "Main.py"])
        newW= Tk()
        newW.title("Stuedent Detail")
        newW.geometry("550x400")
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database = 'sample',
        auth_plugin='mysql_native_password')
        
        mycursor = mydb.cursor()
        exe = "SELECT Name FROM stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="STUDENT DETAILS",relief=RAISED,background = "light blue").place (x=10, y=10)
        Label(newW, text="NAME:").place (x=30, y=50)
        Label(newW, text=res).place (x=160, y=50)
        
        exe = "SELECT address  FROM  stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="PLACE:").place (x=30, y=70)
        Label(newW, text=res).place (x=160, y=70)
        
        exe = "SELECT DOB FROM  stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="DATE OF BIRTH:").place (x=30, y=90)
        Label(newW, text=res).place (x=160, y=90)
        
        exe = "SELECT phonr_no FROM  stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="PHONE NO:").place (x=30, y=110)
        Label(newW, text=res).place (x=160, y=110)
        
        Label(newW, text="STUDENT MARK",relief=RAISED,background = "light blue").place (x=10, y=140)
        exe = "SELECT Physics_Mark FROM  stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="PHYSICS MARK:").place (x=30, y=170)
        Label(newW, text=res).place (x=160, y=170)
        
        exe = "SELECT Maths_Mark FROM  stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="MATHS MARK:").place (x=30, y=200)
        Label(newW, text=res).place (x=160, y=200)
        
        exe = "SELECT Malayalam_Mark FROM  stinfo where Name=%s"
        name=e1.get()
        mycursor.execute(exe,[(name)])
        res = mycursor.fetchall()
        Label(newW, text="MALAYALAM MARK:").place (x=30, y=230)
        Label(newW, text=res).place (x=160, y=230)
        Button(newW, text="Exit", command=newW.destroy,height = 2, width= 10).place(x=450,y=350)
        Button(newW, text="Deactivate",command=dele,height = 2, width= 10).place(x=350,y=350)
        return True

    else:
        messagebox.showinfo("", "Incorrent Username and Password")
        return False

    
def newr():
    r.destroy()
    root=Tk()
    root.title("Login")
    root.geometry("500x300")
    
    Label(root, text="Please Enter The Roll no,Username And Password ",font =('Courier',10, 'bold'),foreground="#0e6ea6").place (x=50, y=10)
    Label(root, text="Roll_No").place (x=10, y=40)
    Label(root, text="UserName").place (x=10, y=70)
    Label(root, text="New Password").place(x=10, y=100)
    
    
    c1 = Entry(root)
    c1.place(x=140, y=40)
    c2=Entry(root)
    c2.place(x=140, y=70)
    c3 = Entry(root)
    c3.place(x=140, y=100)
    def done():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="sample")
        mycursor = mysqldb.cursor()
        d1=c1.get()
        d2=c2.get()
        d3=c3.get()
        sql=("insert into login(Roll_no,admin,passw) values(%s,%s,%s)")
        mycursor.execute(sql,(d1,d2,d3))
        mysqldb.commit()
        print(mycursor.rowcount, "record inserted.")
        
        #Detail Entering
        root=Tk()
        root.title("Login")
        root.geometry("500x400")
        Label(root, text="Personal Information",font =('Courier',14, 'bold'),foreground="#0e6ea6").place (x=100, y=10)
        Label(root, text="Id No").place (x=10, y=40)
        Label(root, text="Name").place (x=10, y=70)
        Label(root, text="Place").place (x=10, y=100)
        Label(root, text="Date Of Birth").place (x=10, y=130)
        Label(root, text="(YYYY-MM-DD)",font=('cooper black', 6)).place (x=10, y=145)
        Label(root, text="Phone_No").place(x=10, y=160)
        Label(root, text="Marks Entering",font =('Courier',14, 'bold'),foreground="#0e6ea6").place (x=100, y=190)
        Label(root, text="Physics Mark").place(x=10, y=220)
        Label(root, text="Maths Mark").place(x=10, y=250)
        Label(root, text="Maths Mark").place(x=10, y=280)
        p1 = Entry(root)
        p1.place(x=140, y=40)
        p2=Entry(root)
        p2.place(x=140, y=70)
        p3 = Entry(root)
        p3.place(x=140, y=160)
        p4=Entry(root)
        p4.place(x=140, y=220)
        p5 = Entry(root)
        p5.place(x=140, y=250)
        p6 = Entry(root)
        p6.place(x=140, y=280)
        p7 = Entry(root)
        p7.place(x=140, y=100)
        p8 = Entry(root)
        p8.place(x=140, y=130)
        def sub():
            if(len(p1.get())==0 or len(p2.get())==0 or len(p3.get())==0 or len(p4.get())==0 or len(p5.get())==0 or len(p6.get())==0 or len(p7.get())==0 or len(p8.get())==0):
                messagebox.showinfo("", "Please complete all required fields")
                
                
            
            
            else:
                mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="sample")
                mycursor = mysqldb.cursor()
                n1=p1.get()
                n2=p2.get()
                n3=p3.get()
                n4=p4.get()
                n5=p5.get()
                n6=p6.get()
                n7=p7.get()
                n8=p8.get()
                sql=("insert into stinfo(id,Name,phonr_no,Physics_mark,Maths_Mark,Malayalam_Mark,DOB,address) values(%s,%s,%s,%s,%s,%s,%s,%s)")
                mycursor.execute(sql,(n1,n2,n3,n4,n5,n6,n8,n7))
                mysqldb.commit()
                print(mycursor.rowcount, "record inserted.")
        Button(root, text="Submitted",command=sub,height = 2, width= 10).place(x=120, y=340)
        Button(root, text="Exit", command=root.destroy,height = 2, width= 10).place(x=280,y=340)
    Button(root, text="DONE",command=done,height = 2, width= 10).place(x=150, y=150)


    

r=Tk()
r.title("Login")
r.geometry("500x300")

global el,e2,p1,p2,p3,p4,p5,p6,p7,p8
global c1,c2,c3

Label(r, text="UserName").place (x=10, y=40)

Label(r, text="Password").place(x=10, y=70)

e1 = Entry(r)
e1.place(x=140, y=50)

e2=Entry(r)
e2.place(x=140, y=80)
e2.config(show="*")
Label(r, text="WELCOME",font =('Courier',14, 'bold'),foreground="#0e6ea6").place (x=200, y=10)
Button(r, text="Login", command=Ok, height = 2, width= 10).place(x=80, y=200)
Button(r, text="New Register",command=newr,height = 2, width= 10).place(x=180, y=200)
Button(r, text="Exit", command=r.destroy,height = 2, width= 4).place(x=350,y=200)


r.mainloop()