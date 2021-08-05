from sqlite3.dbapi2 import Error
from tkinter import *
from tkinter import font
from tkinter.font import BOLD, Font
from sqlofthemain import *
from tkinter import messagebox
import time
def MyClick(rootwindow, whatever):
    MyLabel = Label(rootwindow, text=(f"Hello {whatever.get()}"))
    MyLabel.pack()

def register(regbutton, loggbutton, rootwindow):
    regbutton.destroy()
    loggbutton.destroy()
    usersv = StringVar()
    passwordsv = StringVar()
    lbframe= LabelFrame(rootwindow, relief=FLAT)
    userentry = Entry(lbframe, textvariable=usersv, font=("Arial", 60, "bold"))
    passwordentry= Entry(lbframe,textvariable=passwordsv, font=("Arial", 60, "bold"))
    userentry.pack(padx=200)
    passwordentry.pack(padx=200)
    def register_attempt():
        c.execute("SELECT USER FROM LOGGINDATA")
        userentryvalue = str(usersv.get())
        userentryvalue = str(userentryvalue)
        passwordentryvalue = str(passwordsv.get())
        passwordentryvalue = str(passwordentryvalue)
        for query_result in c.fetchall():
            if userentryvalue in query_result:
                messagebox.showerror(title="Error", message="User already exists") 
            else:
                c.execute("SELECT * FROM LOGGINDATA")
                print(c.fetchall())
                c.execute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)", (userentryvalue, passwordentryvalue))
    confirmregistbutton = Button(lbframe, text='Click Here to Register',font=("Arial", 60, BOLD),relief=GROOVE, padx=220, pady=50, command=lambda: register_attempt()).pack()
    lbframe.pack(padx=200)
    
