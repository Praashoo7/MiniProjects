import charsMod as cm

def main():

    print("A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z")
    print("\n")
    
    print("Press <ENTER> after You're finished typing..\n")
    try:
        n=int(input("To Start Typing, Enter 1 and <ENTER> and Start Typing..\n\n"))
        if n==1:
            print()
            cm.charsMod()
        else:
            print("\nINVALID INPUT")
    except Exception:
        print("\nINVALID INPUT")
  
if __name__=="__main__":
	main()
