import charsModule as cm

def main():

    print("A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z")
    print("\n")
    
    print("Press <ENTER> after You're finished typing..\n")
    
    try:
        cm.charsMod()
    except Exception as c:
        print("\n",c)

if __name__=="__main__":
	main()
