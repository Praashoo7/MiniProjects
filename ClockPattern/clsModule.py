import datetime
import os

def clsModule():

    d=datetime.datetime.now()
    s=d.second
    m=d.minute
    h=d.hour
    
    a=[int(e) for e in str(h)]
    b=[int(e) for e in str(m)]
    c=[int(e) for e in str(s)]
    
    n=5
    
    print(h,end=':')
    print(m,end=':')
    print(s)
    
    print()
    for a1 in range(len(a)):
        for i in range(n):
            for j in range(n):
                if a[a1]==1:
                    if j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==2:
                    if i==0 or i==n-1 or i==n-3 or i==1 and j==4 or i==3 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==3:
                    if i==0 or i==n-1 or i==n-3 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==4:
                    if i==2 and j==1 or j==0 and (i==0 or i==1 or i==2) or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==5:
                    if i==0 or i==2 and (j==0 or j==1 or j==2 or j==3) or i==4 and (j==0 or j==1 or j==2 or j==3) or i==1 and j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==6:
                    if i==0 or i==n-1 or i==n-3 or j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==7:
                    if i==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==8:
                    if i==0 or i==n-1 or i==n-3 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==9:
                    if i==0 or i==n-3 or j==n-1 or i==n-4 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if a[a1]==0:
                    if i==0 or i==n-1 or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                        
            print()
        print("\n")

    for b1 in range(len(b)):
        for i in range(n):
            for j in range(n):
                if b[b1]==1:
                    if j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==2:
                    if i==0 or i==n-1 or i==n-3 or i==1 and j==4 or i==3 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==3:
                    if i==0 or i==n-1 or i==n-3 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==4:
                    if i==2 and j==1 or j==0 and (i==0 or i==1 or i==2) or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==5:
                    if i==0 or i==2 and (j==0 or j==1 or j==2 or j==3) or i==4 and (j==0 or j==1 or j==2 or j==3) or i==1 and j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==6:
                    if i==0 or i==n-1 or i==n-3 or j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==7:
                    if i==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==8:
                    if i==0 or i==n-1 or i==n-3 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==9:
                    if i==0 or i==n-3 or j==n-1 or i==n-4 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if b[b1]==0:
                    if i==0 or i==n-1 or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                        
            print()
        print("\n")
                        
    for c1 in range(len(c)):
        for i in range(n):
            for j in range(n):
                if c[c1]==1:
                    if j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==2:
                    if i==0 or i==n-1 or i==n-3 or i==1 and j==4 or i==3 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==3:
                    if i==0 or i==n-1 or i==n-3 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==4:
                    if i==2 and j==1 or j==0 and (i==0 or i==1 or i==2) or j==n-3:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==5:
                    if i==0 or i==2 and (j==0 or j==1 or j==2 or j==3) or i==4 and (j==0 or j==1 or j==2 or j==3) or i==1 and j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==6:
                    if i==0 or i==n-1 or i==n-3 or j==0 or i==3 and j==4:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==7:
                    if i==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==8:
                    if i==0 or i==n-1 or i==n-3 or j==n-1 or j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==9:
                    if i==0 or i==n-3 or j==n-1 or i==n-4 and j==0:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                
                if c[c1]==0:
                    if i==0 or i==n-1 or j==0 or j==n-1:
                        print("*",end='  ')
                    else:
                        print("",end='    ')
                        
            print()
        print("\n")