def filter(fname,data):

    list=[]
    for i in range(len(data)):
        f=fname(data[i])
        if f==True:
            list.append(data[i])
    return list
    
def map(fname,newdata):                        
    
    list=[]
    for i in range(len(newdata)):
        f=fname(newdata[i])
        list.append(f)
    return list
    
def reduce(fname,incrementdata):

    list=[]
    for i in range(len(incrementdata)):
        if (len(incrementdata))>=2:
            f=fname(incrementdata[0],incrementdata[1])
            del incrementdata[0]
            del incrementdata[0]
            incrementdata.append(f)
            
    return incrementdata[0]
