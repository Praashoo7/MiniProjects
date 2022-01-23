import datetime

def encModule():
    
    s=input("Enter the String : ")
	
    list=[c for c in s]
    n1=len(list)
    
    print()
    if n1>0:
        for d in range(len(list)):
            if list[d]=="A" or list[d]=="a":
                list[d]=".- "
                        
            if list[d]=="B" or list[d]=="b":
                list[d]="-... "
       
            if list[d]=="C" or list[d]=="c":
                list[d]="-.-. "

            if list[d]=="D" or list[d]=="d":
                list[d]="-.. "
                
            if list[d]=="E" or list[d]=="e":
                list[d]=". "
                
            if list[d]=="F" or list[d]=="f":
                list[d]="..-. "
                
            if list[d]=="G" or list[d]=="g":
                list[d]="--. "
                
            if list[d]=="H" or list[d]=="h":
                list[d]=".... "
                
            if list[d]=="I" or list[d]=="i":
                list[d]=".. "
                
            if list[d]=="J" or list[d]=="j":
                list[d]=".--- "
                
            if list[d]=="K" or list[d]=="k":
                list[d]="-.- "
               
            if list[d]=="L" or list[d]=="l":
                list[d]=".-.. "
               
            if list[d]=="M" or list[d]=="m":
                list[d]="-- "
                
            if list[d]=="N" or list[d]=="n":
                list[d]="-. "
                
            if list[d]=="O" or list[d]=="o":
                list[d]="--- "
                
            if list[d]=="P" or list[d]=="p":
                list[d]=".--. "
                
            if list[d]=="Q" or list[d]=="q":
                list[d]="--.- "
                
            if list[d]=="R" or list[d]=="r":
                list[d]=".-. "
                
            if list[d]=="S" or list[d]=="s":
                list[d]="... "
                
            if list[d]=="T" or list[d]=="t":
                list[d]="- "
                
            if list[d]=="U" or list[d]=="u":
                list[d]="..- "
                
            if list[d]=="V" or list[d]=="v":
                list[d]="...- "
                
            if list[d]=="W" or list[d]=="w":
                list[d]=".-- "
                
            if list[d]=="X" or list[d]=="x":
                list[d]="-..- "

            if list[d]=="Y" or list[d]=="y":
                list[d]="-.-- "
                
            if list[d]=="Z" or list[d]=="z":
                list[d]="--.. "
                
            if list[d]=="1" or list[d]=="z":
                list[d]=".---- "
                
            if list[d]=="2" or list[d]=="z":
                list[d]="..--- "
                
            if list[d]=="3" or list[d]=="z":
                list[d]="...-- "
                
            if list[d]=="4" or list[d]=="z":
                list[d]="....- "
                
            if list[d]=="5" or list[d]=="z":
                list[d]="..... "
                
            if list[d]=="6" or list[d]=="z":
                list[d]="-.... "
                
            if list[d]=="7" or list[d]=="z":
                list[d]="--... "
                
            if list[d]=="8" or list[d]=="z":
                list[d]="---.. "
                
            if list[d]=="9" or list[d]=="z":
                list[d]="----. "
                
            if list[d]=="0" or list[d]=="z":
                list[d]="----- "
                
        print(*list, end='')
        
    else:
        print("INVALID") 