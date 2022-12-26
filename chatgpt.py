import tkinter as tk
from tkinter import messagebox
from getpass import getpass
import hashlib
import sqlite3

def hash_password(password):
    # Hash the password using SHA256
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash

def register():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Hash the password
    password_hash = hash_password(password)

    # Store the username and hashed password in the SQLite database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password_hash))
    conn.commit()
    conn.close()

    messagebox.showinfo("Registration", "Registration successful!")

def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Hash the password
    password_hash = hash_password(password)

    # Check if the username and hashed password exist in the SQLite database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password_hash))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Incorrect username or password. Please try again.")

root = tk.Tk()
root.title("Login")

username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=login)
register_button = tk.Button(root, text="Register", command=register)

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0)
register_button.grid(row=2, column=1)

root.mainloop()
