import tkinter as tk

#window specs
win=tk.Tk()
win.title("My Library")
win.geometry('340x440')
win.configure(bg='#333333')

#Creating widgets
loginLabel=tk.Label(win,text="Login")
userLabel=tk.Label(win,text="Username")
passLabel=tk.Label(win,text="Password")
userInput=tk.Entry(win)
passInput=tk.Entry(win,show="*")
loginButton=tk.Button(win,text="Login")

#placing on screen
loginLabel.grid(row=0,column=0,columnspan=3)
userLabel.grid(row=1,column=0)
userInput.grid(row=1,column=1)
passLabel.grid(row=2,column=0)
passInput.grid(row=2,column=1)
loginButton.grid(row=3,column=0,columnspan=3)

win.mainloop()