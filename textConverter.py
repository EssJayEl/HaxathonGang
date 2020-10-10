def pull():
    #pulls data from textfile
    f= open("data1.txt",'r')
    keys = ["grp", "fd", "equity","commodities","realEstate","genExpenses","health","car","electricity","water"]
    l = f.readlines()
    ret = []
    for i in l:
        ret.append(dict())
        #i.rstrip()
        i=i[:-1]
        split = i.split(":")
        #split[-1].rstrip("\n")
        #print(split)
        for j in range(0, len(keys)):
                
                ret[-1][keys[j]] = split[j]
    #print(ret)
    
    return ret
            

def column(n):
    #returns dictionary containing required age group
    ret = pull()
    d = {}
    for i in ret:
        if(i['grp']==n):
            d=i;
    print(d)

#f= open("data1",'r')
#pull()
