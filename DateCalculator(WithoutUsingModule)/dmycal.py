import datetime

import dmycalculateCModule as dc
import dmycalculateMModule as dm

def main():

    print("Select the Date Option : \n")
    d=datetime.datetime.now()
    print("1. Current Date : ",d.year,"-",d.month,"-",d.day)
    print("2. Manual Date\n")
    try:
        n=int(input())
    except Exception:
        print("\nINVALID INPUT")
        quit()
    
    
    if n==1 or n==2:
        if n==1:
            dc.dmycalculateCModule()
        else:
            try:
                myear=int(input("Enter the Manual Year : "))
                mmonth=int(input("Enter the Manual Month : "))
                mdate=int(input("Enter the Manual Day : "))
                dm.dmycalculateMModule(myear,mmonth,mdate)
            except Exception:
                print("\nINVALID INPUT")
                quit()
    else:
        print("\nINVALID INPUT")
        
if __name__=="__main__":
	main()
