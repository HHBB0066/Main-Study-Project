from sqlite3.dbapi2 import Error
from tkinter import *
from tkinter import font
from tkinter.font import BOLD, Font
from sqlofthemain import *
from tkinter import messagebox
import time
import itertools



def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


def cleanWindow(MainWindow):
    widget_list = all_children(MainWindow)
    for item in widget_list:
        item.destroy()


def flatit(listtoflat):    
    flatten = itertools.chain.from_iterable
    listtoflat = list(flatten(listtoflat))
    return listtoflat


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
        inlist = []
        for queryresult in c.fetchall():
            inlist.append(queryresult)
        inlist = flatit(inlist)
        if userentryvalue in inlist:
            messagebox.showerror(title="Error", message="The typed user already exist")
        elif userentryvalue not in inlist:
                c.execute("SELECT * FROM LOGGINDATA")
                c.execute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)", (userentryvalue, passwordentryvalue))
            
    confirmbutton = Button(lbframe, text='Click Here to Register',font=("Arial", 60, BOLD),relief=GROOVE, padx=220, pady=50, command=lambda: register_attempt()).pack()
    lbframe.pack(padx=200)


def loggin(regbutton, loggbutton, rootwindow):
    regbutton.destroy()
    loggbutton.destroy()
    usersv = StringVar()
    passwordsv = StringVar()
    lbframe= LabelFrame(rootwindow, relief=FLAT)
    userentry = Entry(lbframe, textvariable=usersv, font=("Arial", 60, "bold"))
    passwordentry= Entry(lbframe,textvariable=passwordsv, font=("Arial", 60, "bold"))
    userentry.pack(padx=200)
    passwordentry.pack(padx=200)
    def loggin_attempt():
        c.execute("SELECT USER FROM LOGGINDATA")
        userentryvalue = str(usersv.get())
        userentryvalue = str(userentryvalue)
        passwordentryvalue = str(passwordsv.get()) 
        passwordentryvalue = str(passwordentryvalue)
        inlist = []
        for queryresult in c.fetchall():
            inlist.append(queryresult)
        inlist = flatit(inlist)
        if userentryvalue in inlist:
            cleanWindow(rootwindow)
        elif userentryvalue not in inlist:
            messagebox.showerror(title="Error", message="The typed user doesn't exist")
    confirmbutton = Button(lbframe, text='Click Here to Loggin',font=("Arial", 60, BOLD),relief=GROOVE, padx=220, pady=50, command=lambda: loggin_attempt()).pack()
    lbframe.pack(padx=200)




