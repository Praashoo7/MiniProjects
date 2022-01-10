import MagMod as M

def main():        
    
    print(" - Think of a Number from Given Cards and Write the Cards number or numbers on which your chosen number Appears on\n\n - For Example if your chosen number appears on card no 1 and 2 then you write 1<Enter>2 to finish after the last number <Enter>0\n\n - After doing this It will Guess the number that you had thought of.\n\n")


    print("1")
    print("|  8    9   10  11 |\n| 12  13  14  15 |")
    print("")
    print("2")
    print("|  4    5    6    7  |\n| 12  13  14  15 |")
    print("")
    print("3")
    print("|  2    3    6    7  |\n| 10  11  14  15 |")
    print("")
    print("4")
    print("|  1    3    5    7  |\n|  9   11  13  15 |")
    print("")
    
    try:
        M.MagMod()
    except Exception:
        print("\nINVALID")
    
if __name__ == "__main__":
    main()