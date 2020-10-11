import textConverter
import split_page

def salaryFormat(ageGrp,salary):
    row = textConverter.column(ageGrp) #pulled row
    Sum = 0
    li = []
    for i in row:
        if i == 'personalLoan' and row[i]==0:
            base = (6*salary)/30
            row[i] = int(base + base*0.08)
        if i in ["fd","equity","commodities","RealEstate","mortgage"]:
            row[i] = int(salary*row[i]*0.01)
        
        if str(row[i]).isdigit():
            Sum+=row[i]

    a=row["fd"]
    b=row["equity"]
    c=row["commodities"]
    d=row["RealEstate"]
    e=row["healthIns"]
    f=row["vehicleIns"]
    g=row["studentLoan"]
    h=row["personalLoan"]
    i=row["mortgage"]
    j=row["electricity"]
    k=row["water"]
    l=row["rent"]
    m=row["food"]
    n=salary-Sum

    split_page.main_scr(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
    

            
        


    

    #format outputs based on salary and percentages
    #ageGrp is a letter passed to the other file to pick up required dictionary(aka row)
    #salary is given salary
    #returns a dictionary mapping column name to value in Rs
    #if salary not given, returns percetages




