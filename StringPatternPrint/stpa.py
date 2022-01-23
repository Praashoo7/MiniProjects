import stpaModule as sM

def main():
    
    s=input("Enter the String you wanna Print : ")
    
    try:
        sM.stpaModule(s)
    except Exception:
        print("\nINVALID INPUT")
    
if __name__=="__main__":
	main()
