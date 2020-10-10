import textConverter

def salaryFormat(ageGrp, salary = None):
    row = textConverter.column(ageGrp) #pulled row
    ret = dict(row)
    if salary != None:
        for i in ret:
            if i != "grp":
                ret[i] = salary*ret[i]*0.01
        return ret
    else:
        return row

    #format outputs based on salary and percentages
    #ageGrp is a letter passed to the other file to pick up required dictionary(aka row)
    #salary is given salary
    #returns a dictionary mapping column name to value in Rs
    #if salary not given, returns percetages
    
def sliderCalculation(columnName, sliderPercentage, salary, columnDict):
    #adjust other columns based on given columnNumber sliderPercentage
    
