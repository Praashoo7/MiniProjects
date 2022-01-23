def decModule():
    
    str=input("Enter the String : ")
    list1=str.split(" ")
    length=len(str)
    
    if length>0:
        for d in range(len(list1)):
            if list1[d]==".-":
                list1[d]="A"
                     
            if list1[d]=="-...":
                list1[d]="B"
        
            if list1[d]=="-.-.":
                list1[d]="C"

            if list1[d]=="-..":
                list1[d]="D"
               
            if list1[d]==".":
                list1[d]="E"
              
            if list1[d]=="..-.":
                list1[d]="F"
                
            if list1[d]=="--.":
                list1[d]="G"
            
            if list1[d]=="....":
                list1[d]="H"
                
            if list1[d]=="..":
                list1[d]="I"
                
            if list1[d]==".---":
                list1[d]="J"
             
            if list1[d]=="-.-":
                list1[d]="K"
              
            if list1[d]==".-..":
                list1[d]="L"
                
            if list1[d]=="--":
                list1[d]="M"
                
            if list1[d]=="-.":
                list1[d]="N"
                
            if list1[d]=="---":
                list1[d]="O"
                
            if list1[d]==".--.":
                list1[d]="P"
                
            if list1[d]=="--.-":
                list1[d]="Q"
                
            if list1[d]==".-.":
                list1[d]="R"
                
            if list1[d]=="...":
                list1[d]="S"
                
            if list1[d]=="-":
                list1[d]="T"
                    
            if list1[d]=="..-":
                list1[d]="U"
                
            if list1[d]=="...-":
                list1[d]="V"
                
            if list1[d]==".--":
                list1[d]="W"
                
            if list1[d]=="-..-":
                list1[d]="X"

            if list1[d]=="-.--":
                list1[d]="Y"
                
            if list1[d]=="--..":
                list1[d]="Z"
        
            if list1[d]==".----":
                list1[d]="1"
        
            if list1[d]=="..---":
                list1[d]="2"
        
            if list1[d]=="...--":
                list1[d]="3"
        
            if list1[d]=="....-":
                list1[d]="4"
        
            if list1[d]==".....":
                list1[d]="5"
        
            if list1[d]=="-....":
                list1[d]="6"
        
            if list1[d]=="--...":
                list1[d]="7"
        
            if list1[d]=="---..":
                list1[d]="8"
        
            if list1[d]=="----.":
                list1[d]="9"
        
            if list1[d]=="-----":
                list1[d]="0"
        
            if list1[d]=="/":
                list1[d]=" "
                
        print(*list1, end='')

    else:
        print("INVALID") 