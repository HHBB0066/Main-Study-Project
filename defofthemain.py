from sqlite3.dbapi2 import Error
from tkinter import *
from tkinter import font
from tkinter.font import BOLD, Font
from sqlofthemain import *
from tkinter import messagebox
import time
import itertools

def selectUser():
    c.execute("SELECT USER FROM LOGGINDATA")

def selectPassword():
    c.execute("SELECT PASSWORD FROM LOGGINDATA")

def runLoginWindow():
    logginwindow = Tk()
    logginwindow.state('zoomed')
    logginwindow.title('Loggin')
    logginwindow.iconbitmap
    logginwindow.resizable(height=False, width=False)


    registerbutton = Button(logginwindow, text=('register'), font=('Arial', 40, 'bold'), padx=600, pady=150,
                            bg='white', justify="center", command=lambda: register(registerbutton, logginbutton, logginwindow))

    logginbutton = Button(logginwindow, text="loggin", font=("Arial", 40, "bold"), padx=620,
                          pady=150, bg='white', command=lambda: loggin(registerbutton, logginbutton, logginwindow))
    registerbutton.grid()
    logginbutton.grid()
    logginwindow.update()
    windowname = 'Menu'
    logginwindow.mainloop()

    
class ValueIsEmptyError(Error):
    """Raised when there is nothing in the entry input field"""
    pass

# def entryValueChecker(entry, entry2):
#     """
#         It's gonna return True if there is nothing, or it's gonna return False if there is anithyng.

#     """
#     if (entry.isspace() == True or entry == "") or (entry2.isspace() == True or entry2 == ""):
#         return True
#     else:
#         return False

# class valueIsEmpty(Exception):
#     def __init__(self, message, entry, entry2):
#        super().__init__(message)
#        entryValueChecker().__init__(entry, entry2)
#        self.entry = entry
#        self.entry2 = entry2
#        if entryValueChecker(entry, entry2) == True:
#            raise valueIsEmpty(message="You have to put something on the entry", entry=entry, e2=entry2)

def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list




def cleanWindow(MainWindow):
    widget_list = all_children(MainWindow)
    for item in widget_list:
        item.destroy()

def registernow(mainwindow,usrentv,pwdentv):
    if (not usrentv or pwdentv == "") or (not usrentv.isspace() or pwdentv.isspace()):


        c.execute("SELECT * FROM LOGGINDATA")
        print("Something just for a simple test")
        c.execute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)",
                  (usrentv, pwdentv))
        messagebox.showinfo(title="Successful",
                            message="Successfully Registered")
        cleanWindow(mainwindow)
        mainwindow.update()
    else:
        messagebox.showerror(title="Value is Empty", message="Please insert something on both entry fields")
        raise ValueIsEmptyError

def flatit(listtoflat):
    flatten = itertools.chain.from_iterable
    listtoflat = list(flatten(listtoflat))
    return listtoflat


def usersList():
    selectUser()
    userinlist = []
    for queryresult in c.fetchall():
        userinlist.append(queryresult)
    userinlist = flatit(userinlist)
    return userinlist


def passwordList():
    selectPassword()
    passwordinlist = []
    for queryresult in c.fetchall():
        passwordinlist.append(queryresult)
    passwordinlist = flatit(passwordinlist)
    return passwordinlist


def MyClick(rootwindow, whatever):
    MyLabel = Label(rootwindow, text=(f"Hello {whatever.get()}"))
    MyLabel.grid()


def register(regbutton, loggbutton, rootwindow):
    regbutton.destroy()
    loggbutton.destroy()
    usersv = StringVar()
    passwordsv = StringVar()
    lbframe = LabelFrame(rootwindow, relief=FLAT)
    userentry = Entry(lbframe, textvariable=usersv, font=("Arial", 60, "bold"))
    passwordentry = Entry(lbframe, textvariable=passwordsv,
                          font=("Arial", 60, "bold"))
    userentry.grid()
    passwordentry.grid()

    def register_attempt():
        selectUser()
        userentryvalue = str(usersv.get())
        userentryvalue = str(userentryvalue)
        passwordentryvalue = str(passwordsv.get())
        passwordentryvalue = str(passwordentryvalue)
        userinlist = usersList()
        passwordinlist = passwordList()
        x = userentryvalue
        y = passwordentryvalue
        if (userentryvalue in userinlist): #and (passwordentryvalue in passwordinlist)
            messagebox.showerror(
                title="Error", message="The typed user already exist")
        elif (userentryvalue not in userinlist) or (passwordentryvalue not in passwordinlist):
            while True:
            #     time.sleep(5)
                # errorobject = valueIsEmpty(message="We got a error", entry=x, entry2=y)
                try:
                    rootwindow.update()
                    if (x or y == "") or (x.isspace() or y.isspace() == True):
                        raise ValueIsEmptyError
                    # c.execute("SELECT * FROM LOGGINDATA")
                    # print("Something just for a simple test")
                    # c.exe-cute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)",
                    #           (userentryvalue, passwordentryvalue))
                    # messagebox.showinfo(title="Successful",
                    #                     message="Successfully Registered")
                    # cleanWindow(rootwindow)
                    # rootwindow.update()
                except ValueIsEmptyError:
                    print("Please, fill in the fields")
                    # rootwindow.update()
                    print("Error: It should be something in the entry")
                    messagebox.showerror(title="Error", message="It should be something on the entry field")
                    break
                print('deu certo')
                registernow(mainwindow=rootwindow, usrentv=x, pwdentv=y)
                
        # register_attempt()
    windowname = 'Register_Window'
    confirmbutton = Button(lbframe, text='Click Here to Register', font=("Arial", 60, BOLD), relief=GROOVE, padx=220, pady=50, command=lambda: register_attempt()).grid()
    lbframe.grid()


def loggin(regbutton, loggbutton, rootwindow):
    regbutton.destroy()
    loggbutton.destroy()
    usersv = StringVar()
    passwordsv = StringVar()
    lbframe = LabelFrame(rootwindow, relief=FLAT)
    userentry = Entry(lbframe, textvariable=usersv, font=("Arial", 60, "bold"))
    passwordentry = Entry(lbframe, textvariable=passwordsv,
                          font=("Arial", 60, "bold"))
    userentry.grid()
    passwordentry.grid()

    def loggin_attempt():
        selectUser()
        userentryvalue = str(usersv.get())
        userentryvalue = str(userentryvalue)
        passwordentryvalue = str(passwordsv.get())
        passwordentryvalue = str(passwordentryvalue)
        userinlist = []
        passwordinlist = []
        for queryresult in c.fetchall():
            userinlist.append(queryresult)
        inlist = flatit(userinlist)
        for queryresult in c.fetchall():
            passwordinlist.append(queryresult)
        passwordinlist = flatit(inlist)
        if userentryvalue in inlist:
            cleanWindow(rootwindow)
        elif userentryvalue not in inlist:
            messagebox.showerror(
                title="Error", message="The typed user doesn't exist")
    windowname = 'Loggin_Window'
    confirmbutton = Button(lbframe, text='Click Here to Loggin', font=(
        "Arial", 60, BOLD), relief=GROOVE, padx=220, pady=50, command=lambda: loggin_attempt()).grid()
    lbframe.grid()

    # for query_result in c.fetchall():
    #         if userentryvalue not in query_result:
    #             # messagebox.showerror(title="Error", message="User doesn't exist, please come back and register")
    #             notinlist = []
    #             notinlist.append(query_result)
    #             if userentryvalue in notinlist:
    #                 widget_list = all_children(rootwindow)
    #                 for item in widget_list:
    #                     item.destroy()

    #             else:
    #                 messagebox.showerror(title="Error", message="User does not exists")
    #             print(notinlist)


# widget_list = all_children(rootwindow)
#                 for item in widget_list:
#                         item.destroy()
#             elif userentryvalue not in query_result:
#                 messagebox.showerror(title="Error", message="User doesn't exist, please come back and register")
