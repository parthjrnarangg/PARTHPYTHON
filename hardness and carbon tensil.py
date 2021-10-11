hardness=int(input("enter your  hardness"))
carbon=float(input("enter your carbon"))
tensil=int (input("enter your tensil strenght"))

first=50
second=0.7
three=5600

if first==hardness and second==carbon and three==tensil:
    print("the score is 9")
            
elif first==hardness and second==carbon:
    print("the score is 7")
    
elif three==tensil and second==carbon:
    print("the score is 8")
    
elif first==hardness:
    print("the score is 6")
               
elif first==hardness:
    print("the score is 5")
               
elif second==carbon:
    print("the score is 5")
            
elif three==tensil:
    print("the score is 5")
    
             

            
