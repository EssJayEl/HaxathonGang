from tkinter import *
import backend_module

def input_as(age,sal):
    x=""
    if age=='21-28':
        x="A"
    elif age=='29-35':
        x="B"
    elif age=='36-42':
        x="C"
    elif age=='43-48':
        x="D"
    sal = int(sal)

    backend_module.salaryFormat(x,sal)


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

Age_L = Label(Form, text = "       ENTER YOUR AGE", font=('arial', 14), bd=16)

Age_L.config(foreground='black')

Age_L.grid(row=3,column=1, sticky="e")

Sal_L = Label(Form, text = "ENTER YOUR MONTHLY SALARY", font=('arial', 14), bd=15)

Sal_L.config(foreground='black')

Sal_L.grid(row=4,column=1, sticky="e")

age=StringVar()
age.set('21-28')

Age_I = OptionMenu(Form,age,*['21-28','29-35','36-42','43-48'])
Age_I.config(height=2,width=30)
Age_I.grid(row=3, column=2)

Sal_I= Entry(Form, font=(14))
Sal_I.grid(row=4, column=2)
HT1=Button(Form, text="SUBMIT" , width=45,height=4,command=lambda:input_as(age.get(),Sal_I.get()))
HT1.grid(row=5, column=2)
HT1.config(background="white")
title.pack(fill=X)

root.mainloop()

