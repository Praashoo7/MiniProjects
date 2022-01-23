import encIMModule as em
import decIMModule as dm

def main():
    
    print("1. To Morce")
    print("2. From Morce\n\n")
    
    n=int(input("Enter your Choice : "))
    
    if n==1:
        em.encModule()
    elif n==2:
        dm.decModule()
    else:
        print("Invalid Input")

if __name__=="__main__":
	main()
