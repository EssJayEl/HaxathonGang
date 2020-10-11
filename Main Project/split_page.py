from tkinter import *

def main_scr(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    screen=Tk()
    screen.title("SPLIT")

    #Investment
    inv_label=Label(screen,text="INVESTMENT").grid(row=0,column=3)
    fd_label=Label(screen,text="FD").grid(row=2,column=0)
    equ_label=Label(screen,text="Equity").grid(row=2,column=2)
    com_label=Label(screen,text="Commodity").grid(row=2,column=4)
    re_label=Label(screen,text="Real Estate").grid(row=2,column=6)
    fd_sli=Scale(screen,from_=1,to=a,orient=HORIZONTAL)
    fd_sli.set(a)
    fd_sli.grid(row=3,column=0)
    
    equ_sli=Scale(screen,from_=1,to=b,orient=HORIZONTAL)
    equ_sli.set(b)
    equ_sli.grid(row=3,column=2)
    com_sli=Scale(screen,from_=1,to=c,orient=HORIZONTAL)
    com_sli.set(c)
    com_sli.grid(row=3,column=4)
    re_sli=Scale(screen,from_=1,to=d,orient=HORIZONTAL)
    re_sli.set(d)
    re_sli.grid(row=3,column=6)


    #Insurance
    ins_label=Label(screen,text="INSURANCE").grid(row=6,column=3)
    hea_label=Label(screen,text="Health").grid(row=7,column=1)
    veh_label=Label(screen,text="Vehicle").grid(row=7,column=5)
    hea_sli=Scale(screen,from_=1,to=e,orient=HORIZONTAL)
    hea_sli.set(e)
    hea_sli.grid(row=8,column=1)
    veh_sli=Scale(screen,from_=1,to=f,orient=HORIZONTAL)
    veh_sli.set(f)
    veh_sli.grid(row=8,column=5)

    #Loans

    if g!=0:
        stu_label=Label(screen,text="Student").grid(row=11,column=1)
        stu_sli=Scale(screen,from_=1,to=g,orient=HORIZONTAL)
        stu_sli.set(g)
        stu_sli.grid(row=12,column=1)

    if i!=0:
        mor_label=Label(screen,text="Mortgage").grid(row=11,column=5)
        mor_sli=Scale(screen,from_=1,to=i,orient=HORIZONTAL)
        mor_sli.set(i)
        mor_sli.grid(row=12,column=5)
    lo_label=Label(screen,text="LOANS").grid(row=10,column=3)    
    per_label=Label(screen,text="Personal").grid(row=11,column=3)
    
    
    per_sli=Scale(screen,from_=1,to=h,orient=HORIZONTAL)
    per_sli.set(h)
    per_sli.grid(row=12,column=3)
    


    #Bills
    
    if l!=0:
        rent_label=Label(screen,text="Rent").grid(row=15,column=5)
        rent_sli=Scale(screen,from_=1,to=l,orient=HORIZONTAL)
        rent_sli.set(l)
        rent_sli.grid(row=16,column=5)

    
    bi_label=Label(screen,text="BILLS").grid(row=14,column=3)
    ele_label=Label(screen,text="Electricity").grid(row=15,column=1)
    wat_label=Label(screen,text="Water").grid(row=15,column=3)
    
    ele_sli=Scale(screen,from_=1,to=j,orient=HORIZONTAL)
    ele_sli.set(j)
    ele_sli.grid(row=16,column=1)
    wat_sli=Scale(screen,from_=1,to=k,orient=HORIZONTAL)
    wat_sli.set(k)
    wat_sli.grid(row=16,column=3)
    

    #Expenses


    if n!=0:
        misc_label=Label(screen,text="Miscellaneous").grid(row=19,column=5)
        misc_sli=Scale(screen,from_=1,to=n,orient=HORIZONTAL)
        misc_sli.set(n)
        misc_sli.grid(row=20,column=5)

    exp_label=Label(screen,text="EXPENSES").grid(row=18,column=3)
    food_label=Label(screen,text="Food").grid(row=19,column=1)
    
    food_sli=Scale(screen,from_=1,to=m,orient=HORIZONTAL)
    food_sli.set(m)
    food_sli.grid(row=20,column=1)
    


    screen.mainloop()
