#There is a simpler way to do this.

def MagModule(): 
   
    while True:
        n=int(input("Enter the Number of Card : "))
        if n!=0:
            n1=int(input("Again? : "))
        else:
            print("INVALID")
            break
        if n1!=0:
            n2=int(input("Enter Again : "))
        else:
            if n==1:
                E=8
                print("Your Number is : ",E)
            elif n==2:
                E=4
                print("Your Number is : ",E)
            elif n==3:
                E=2
                print("Your Number is : ",E)
            else:
                E=1
                print("Your Number is : ",E)
            break
        if n2!=0:
            n3=int(input("Enter Again : "))
        else:
            if n==1 and n1==2:
                E=12
                print("Your Number is : ",E)
            elif n==1 and n1==3:
                E=10
                print("Your Number is : ",E)
            elif n==1 and n1==4:
                E=9
                print("Your Number is : ",E)
            elif n==2 and n1==1:
                E=12
                print("Your Number is : ",E)
            elif n==2 and n1==3:
                E=6
                print("Your Number is : ",E)
            elif n==2 and n1==4:
                E=5
                print("Your Number is : ",E)
            elif n==3 and n1==1:
                E=10
                print("Your Number is : ",E)
            elif n==3 and n1==2:
                E=6
                print("Your Number is : ",E)
            elif n==3 and n1==4:
                E=3
                print("Your Number is : ",E)
            elif n==4 and n1==1:
                E=9
                print("Your Number is : ",E)
            elif n==4 and n1==2:
                E=5
                print("Your Number is : ",E)
            else:
                E=3
                print("Your Number is : ",E)
            break
        if n3!=0:
            if n==1 and n1==2 and n2==3 and n3==4:
                E=15
                print("Your Number is : ",E)
            elif n==1 and n1==2 and n2==4 and n3==3:
                E=15
                print("Your Number is : ",E)
            elif n==1 and n1==3 and n2==2 and n3==4:
                E=15
                print("Your Number is : ",E)
            elif n==1 and n1==3 and n2==4 and n3==2:
                E=15
                print("Your Number is : ",E)
            elif n==1 and n1==4 and n2==2 and n3==3:
                E=15
                print("Your Number is : ",E)
            elif n==1 and n1==4 and n2==3 and n3==2:
                E=15
                print("Your Number is : ",E)
            elif n==2 and n1==1 and n2==3 and n3==4:
                E=15
                print("Your Number is : ",E)
            elif n==2 and n1==1 and n2==4 and n3==3:
                E=15
                print("Your Number is : ",E)
            elif n==2 and n1==3 and n2==1 and n3==4:
                E=15
                print("Your Number is : ",E)
            elif n==2 and n1==3 and n2==4 and n3==1:
                E=15
                print("Your Number is : ",E)
            elif n==2 and n1==4 and n2==1 and n3==3:
                E=15
                print("Your Number is : ",E)
            elif n==2 and n1==4 and n2==3 and n3==1:
                E=15
                print("Your Number is : ",E)
            elif n==3 and n1==1 and n2==2 and n3==4:
                E=15
                print("Your Number is : ",E)
            elif n==3 and n1==1 and n2==4 and n3==2:
                E=15
                print("Your Number is : ",E)
            elif n==3 and n1==2 and n2==1 and n3==4:
                E=15
                print("Your Number is : ",E)
            elif n==3 and n1==2 and n2==4 and n3==1:
                E=15
                print("Your Number is : ",E)
            elif n==3 and n1==4 and n2==1 and n3==2:
                E=15
                print("Your Number is : ",E)
            elif n==3 and n1==4 and n2==2 and n3==1:
                E=15
                print("Your Number is : ",E)
            elif n==4 and n1==1 and n2==2 and n3==3:
                E=15
                print("Your Number is : ",E)
            elif n==4 and n1==1 and n2==3 and n3==2:
                E=15
                print("Your Number is : ",E)
            elif n==4 and n1==2 and n2==1 and n3==3:
                E=15
                print("Your Number is : ",E)
            elif n==4 and n1==2 and n2==3 and n3==1:
                E=15
                print("Your Number is : ",E)
            elif n==4 and n1==3 and n2==1 and n3==2:
                E=15
                print("Your Number is : ",E)
            else:
                E=15
                print("Your Number is : ",E)
            break
        else:
            if n==1 and n1==2 and n2==3:
                E=14
                print("Your Number is : ",E)
            elif n==1 and n1==3 and n2==2:
                E=14
                print("Your Number is : ",E)
            elif n==1 and n1==4 and n2==2:
                E=13
                print("Your Number is : ",E)
            elif n==1 and n1==2 and n2==4:
                E=13
                print("Your Number is : ",E)
            elif n==1 and n1==3 and n2==4:
                E=11
                print("Your Number is : ",E)
            elif n==1 and n1==4 and n2==3:
                E=11
                print("Your Number is : ",E)
            elif n==2 and n1==3 and n2==1:
                E=14
                print("Your Number is : ",E)
            elif n==3 and n1==2 and n2==1:
                E=14
                print("Your Number is : ",E)
            elif n==4 and n1==2 and n2==1:
                E=13
                print("Your Number is : ",E)
            elif n==2 and n1==4 and n2==1:
                E=13
                print("Your Number is : ",E)
            elif n==3 and n1==4 and n2==1:
                E=11
                print("Your Number is : ",E)
            elif n==4 and n1==3 and n2==1:
                E=11
                print("Your Number is : ",E)
            elif n==2 and n1==1 and n2==3:
                E=14
                print("Your Number is : ",E)
            elif n==3 and n1==1 and n2==2:
                E=14
                print("Your Number is : ",E)
            elif n==4 and n1==1 and n2==2:
                E=13
                print("Your Number is : ",E)
            elif n==2 and n1==1 and n2==4:
                E=13
                print("Your Number is : ",E)
            elif n==3 and n1==1 and n2==4:
                E=11
                print("Your Number is : ",E)
            elif n==4 and n1==1 and n2==3:
                E=11
                print("Your Number is : ",E)
            elif n==2 and n1==4 and n2==3:
                E=7
                print("Your Number is : ",E)
            elif n==2 and n1==1 and n2==3:
                E=14
                print("Your Number is : ",E)
            elif n==2 and n1==3 and n2==4:
                E=7
                print("Your Number is : ",E)
            elif n==3 and n1==2 and n2==4:
                E=7
                print("Your Number is : ",E)
            elif n==4 and n1==2 and n2==3:
                E=7
                print("Your Number is : ",E)
            elif n==4 and n1==3 and n2==2:
                E=7
                print("Your Number is : ",E)
            else:
                E=7
                print("Your Number is : ",E)
            break
