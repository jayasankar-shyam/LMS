from tkinter import* 
from tkinter import messagebox
import mysql.connector

conn=mysql.connector.connect(host='localhost',password='pass',user='root',database='library')
cur=conn.cursor()
root=Tk()
title="Login"
root.title(title)
root.geometry("450x500+500+200")
root.configure(bg="")
root.resizable(False,False)

# Frame of the GUI
# img = PhotoImage(file="login.png")
Label(root, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=55, y=70)

# Sign in Header
heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
heading.place(x=100, y=5)

# User entry box

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0,"Username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
user.place(x=30, y=80)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Password entry box
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name=code.get()
    if name == "":
        code.insert(0,"Password")


code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
code.place(x=30, y=150)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Sign in Button 
def sign_in():
    username=user.get()
    password=code.get()

    sql = "select * from users where username = %s and password = %s"
    cur.execute(sql, [(username), (password)])
    results = cur.fetchall()

    if username == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("Application")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen, text="Data Structure \nand \nAlgorithm", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)

        screen.mainloop

    elif username != "admin" and password != "1234":
        messagebox.showerror("Invalid", "Invalid username and password")
    elif password != "1234":
        messagebox.showerror("Invalid", "Invalid password")
    


Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=sign_in).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft Yahei Light",9))
label.place(x=75, y=270)

# Sign up Button
sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=215, y=270)

root.mainloop()