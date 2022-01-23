import encIMModule as em
import decIMModule as dm

def main():
    
    print("1. To Morce")
    print("2. From Morce\n\n")
    try:
        n=int(input("Enter your Choice : "))
    except Exception:
        print("\nINVALID INPUT")
        quit()
    
    if n==1:
        em.encModule()
    elif n==2:
        dm.decModule()
    else:
        print("\nINVALID INPUT")

if __name__=="__main__":
	main()