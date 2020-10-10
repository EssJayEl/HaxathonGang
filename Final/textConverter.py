def pull():
    #pulls data from textfile
    f= open("data1.txt",'r')
    keys = ["agegrp","fd","equity","commodities","RealEstate","healthIns","vehicleIns","studentLoan","personalLoan","mortgage","electricity","water","rent","food"]
    l = f.readlines()
    ret = []
    for i in l:
        ret.append(dict())
        i=i[:-1]
        split = i.split(":")
        for j in range(0, len(keys)):
                if split[j].isdigit():
                    split[j] = int(split[j])
                ret[-1][keys[j]] = split[j]
    
    return ret
            

def column(n):
    #returns dictionary containing required age group
    ret = pull()
    d = {}
    for i in ret:
        if(i['agegrp']==n):
            d=i
    return(d)

