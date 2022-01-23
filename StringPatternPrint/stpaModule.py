def stpaModule(s):

    list=[c for c in s]
    
    n=5
    
    print()
    for d in range(len(list)):
        for i in range(n):
            for j in range(n):
                if list[d]=="A" or list[d]=="a":
                    if i==0 or i==n-3 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                        
                if list[d]=="B" or list[d]=="b":
                    if i==0 or i==n-3 or i==n-1 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                        
                if list[d]=="C" or list[d]=="c":
                    if i==0 or i==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="D" or list[d]=="d":
                    if i==0 or i==n-1 or j==n-1 or j==n-4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="E" or list[d]=="e":
                    if i==0 or i==n-1 or i==n-3 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="F" or list[d]=="f":
                    if i==0 or i==n-3 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="G" or list[d]=="g":
                    if i==0 or i==n-1 or j==0 or j==n-1 and (i==n-3 or i==n-2) or i==2 and (j==n-3 or j==n-2):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="H" or list[d]=="h":
                    if i==n-3 or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="I" or list[d]=="i":
                    if i==0 or i==n-1 or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="J" or list[d]=="j":
                    if i==0 or i==4 and (j==0 or j==n-4) or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="K" or list[d]=="k":
                    if i+j==3 or i-j==1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="L" or list[d]=="l":
                    if i==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="M" or list[d]=="m":
                    if (i==1 and j==1 or i==2 and j==2 or i==1 and j==3) or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="N" or list[d]=="n":
                    if i==j or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="O" or list[d]=="o":
                    if j==0 and (i==1 or i==2 or i==3) or i==0 and (j==1 or j==2 or j==3) or j==n-1 and (i==1 or i==2 or i==3) or i==n-1 and (j==1 or j==2 or j==3) :
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="P" or list[d]=="p":
                    if i==0 or i==n-3 or j==n-1 and (i==0 or i==n-4 or i==n-3) or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="Q" or list[d]=="q":
                    if i==0 or i==n-3 or j==0 and (i==0 or i==n-4 or i==n-3) or j==n-1 and (i==0 or i==n-4 or i==n-3) or i==n-2 and j==n-2 or i==n-1 and j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="R" or list[d]=="r":
                    if i==0 or j==4 and (i==0 or i==1 or i==2) or i==2 and (j==2 or j==3) or i==3 and j==3 or i==4 and j==4 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="S" or list[d]=="s":
                    if i==0 or i==n-1 or i==n-3 or i==1 and j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="T" or list[d]=="t":
                    if i==0 or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="U" or list[d]=="u":
                    if i==n-1 or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="V" or list[d]=="v":
                    if (i-j==2) or i==3 and j==3 or i==2 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="W" or list[d]=="w":
                    if i==2 and j==2 or i==3 and j==3 or i==3 and j==1 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="X" or list[d]=="x":
                    if i==j or i+j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="Y" or list[d]=="y":
                    if i==0 and j==4 or i==1 and j==3 or i==0 and j==0 or i==1 and j==1 or i==2 and j==2 or j==2 and (i==2 or i==3 or i==4):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="Z" or list[d]=="z":
                    if i==0 or i==n-1 or (i+j==n-1):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="1":
                    if j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="2":
                    if i==0 or i==n-1 or i==n-3 or i==1 and j==4 or i==3 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="3":
                    if i==0 or i==n-1 or i==n-3 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="4":
                    if i==2 and j==1 or j==0 and (i==0 or i==1 or i==2) or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="5":
                    if i==0 or i==2 and (j==0 or j==1 or j==2 or j==3) or i==4 and (j==0 or j==1 or j==2 or j==3) or i==1 and j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="6":
                    if i==0 or i==n-1 or i==n-3 or j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="7":
                    if i==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="8":
                    if i==0 or i==n-1 or i==n-3 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="9":
                    if i==0 or i==n-3 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="0":
                    if i==0 or i==n-1 or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="!":
                    if j==2 and (i==0 or i==1 or i==2 or i==4):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="$":
                    if i==1 and (j==1 or j==2 or j==3) or i==2 and (j==1 or j==2 or j==3) or i==3 and (j==1 or j==2 or j==3) or j==2:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="%":
                    if i+j==n-1 or i==1 and j==1 or i==3 and j==3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="^":
                    if i+j==2 or i==1 and j==3 or i==2 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="*":
                    if i+j==n-1 or i==j or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="(":
                    if i==0 and j==2 or i==4 and j==2 or j==1 and (i==1 or i==2 or i==3):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]==")":
                    if i==0 and j==2 or i==4 and j==2 or j==3 and (i==1 or i==2 or i==3):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="-":
                    if i==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="+":
                    if i==n-3 or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="`":
                    if i==0 and j==1 or i==1 and j==2:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="~":
                    if i+j==1 or i==1 and j==2 or i==0 and j==3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="[":
                    if i==0 and j==1 or i==4 and j==1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="]":
                    if i==0 and j==3 or i==4 and j==3 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="/":
                    if i+j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="?":
                    if i==0 and (j==1 or j==2 or j==3) or i==1 and (j==2 or j==3) or i==2 and j==2 or i==4 and j==2:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]==">":
                    if j-i==2 or i+j==6:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="<":
                    if j+i==2 or i-j==2:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]==";":
                    if j==2 and (i==0 or i==2 or i==3) or i==4 and j==1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]==":":
                    if j==2 and (i==1 or i==2):
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]==",":
                    if j==2 and (i==2 or i==3) or i==4 and j==1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="|":
                    if j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]==".":
                    if i==4 and j==1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="{":
                    if j==1 and (i==0 or i==1 or i==3 or i==4) or i==2 and j==0 or i==0 and j==2 or i==4 and j==2:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if list[d]=="}":
                    if j==3 and (i==0 or i==1 or i==3 or i==4) or i==2 and j==4 or i==0 and j==2 or i==4 and j==2:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                        
            print()
        print("\n")      