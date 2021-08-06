from tkinter import *
from defofthemain import *

logginwindow = Tk()
logginwindow.state('zoomed')
logginwindow.title('Loggin')
logginwindow.iconbitmap
logginwindow.resizable(height=False, width=False)


registerbutton = Button(logginwindow, text=('register'), font=('Arial', 40, 'bold'), padx=600, pady=150, bg='white', justify= "center", command=lambda: register(registerbutton, logginbutton, logginwindow))

logginbutton = Button(logginwindow, text="loggin", font=("Arial", 40, "bold"), padx=620, pady=150, bg='white', command=lambda: loggin(registerbutton, logginbutton, logginwindow))
registerbutton.grid()
logginbutton.grid()
logginwindow.update()

logginwindow.mainloop()


root = Tk()
# root.geometry("500x300+450+250")
root.title("Personal Database")
root.state('zoomed')
# root.iconbitmap("C:/Users/Guilherme/Downloads/personaldata_Msh_icon.ico")
icon = PhotoImage(file="C:/Users/Guilherme/Desktop/personaldata.png")
root.iconphoto(True, icon)
root.config(background="White") # or u can also put instead of black the hex code of some color u want
Name_label = Label(root, width=20, height=10, text="CDB PANEL")
Name_label.grid(row= 0, column=0)

conn.commit()
conn.close()
