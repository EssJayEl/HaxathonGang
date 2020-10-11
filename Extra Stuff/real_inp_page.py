from tkinter import *

root = Tk()
root.destroy()
root = Tk()
root.title("NZXT: Licenced to- x ")
width =  700
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
Form.config(background='light blue')
root.config(background='light blue')
Top.config(background='light blue')

title = Label(Top, text = "WELCOME USER", font=('arial', 15))
title.pack(fill=X)
blank=Label(Form,text="")
blank.config(background='light blue')

blank.grid(row=2,column=1,columnspan=10)
title.config(background='light blue')

username = Label(Form, text = "       ENTER YOUR AGE", font=('arial', 14), bd=16)
#username.config(background="black")
username.config(foreground='black')

username.grid(row=3,column=1, sticky="e")

password = Label(Form, text = "ENTER YOUR SALARY", font=('arial', 14), bd=15)
#password.config(background="black")
password.config(foreground='black')

password.grid(row=4,column=1, sticky="e")

username = Entry(Form,font=(14))
username.grid(row=3, column=2)

password= Entry(Form, font=(14))
password.grid(row=4, column=2)
HT1=Button(Form, text="SUBMIT" , width=45,height=4,command="""#JAWWAD ENTER CODE#""")
HT1.grid(row=5, column=2)
HT1.config(background="white")
title.pack(fill=X)

