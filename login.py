import tkinter as tk
from tkinter import messagebox

#window specs
bg="#333333"
fg="#ffffff"
win=tk.Tk()
win.title("My Library")
win.geometry('640x360')
win.configure(bg=bg)
frame=tk.Frame(bg=bg)

def login():
    username="test"
    password="pass"
    if userInput.get()==username and passInput.get()==password:
        messagebox.showinfo(title="Login Successfull !!",message="You have successfully logged in.")
    else:
        messagebox.showerror(title="Login Failed !!",message="Please check your credentials.")

#Creating widgets
loginLabel=tk.Label(frame,text="Login",bg=bg,fg=fg,font=("Arial",30))
userLabel=tk.Label(frame,text="Username",bg=bg,fg=fg,font=("Arial",16))
passLabel=tk.Label(frame,text="Password",bg=bg,fg=fg,font=("Arial",16))
userInput=tk.Entry(frame,font=("Arial",16))
passInput=tk.Entry(frame,show="*",font=("Arial",16))
loginButton=tk.Button(frame,text="Login",fg=fg,bg="#f35e46",font=("Arial",16),command=login)

#placing on screen
loginLabel.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
userLabel.grid(row=1,column=0,pady=10)
userInput.grid(row=1,column=1)
passLabel.grid(row=2,column=0,pady=10)
passInput.grid(row=2,column=1)
loginButton.grid(row=3,column=0,columnspan=2,pady=20)
frame.pack()
win.mainloop()
printf(hello)