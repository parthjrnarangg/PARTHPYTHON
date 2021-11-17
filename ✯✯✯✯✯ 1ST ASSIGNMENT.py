print("✩✩LIST OF MY FUNCTIONS✩✩")
print("1st : Find simple interest")
print("2nd : Swap between two numbers")
print("3rd : Find your net salary ")
print("4th : Find sum of digits of four digit number ")
print("5th : Find your maturity")
print("6th : Find profit loss ")
print("7th : KM in all units")
print("8th : Convert temperature to celcius")
print("9th : Find your number is odd or even")

print("✯✯TO OPEN PROGRAM TYPE (function1st,function2nd,function3rd)✯✯")

def function1st():
     P=int(input("Enter your Principal"))
     R=int(input("Enter your Rate"))
     T=int(input("Enter your Time"))
     total = P*R*T
     print("SIMPLE INTEREST IS ",total)




def function2nd():
    X = input("enter value of x ")
    Y = input("enter value of y")
    temp = X
    X=Y
    Y = temp
    print("value of X",X)
    print("value of Y",Y)





def function3rd():
    BS = int(input("Enter your basic salary"))
    total = BS + (BS/10*4) + (BS/10) - (BS/10*0.5)
    print("Net Salary is ", total)






def function4th():
    num = int(input("enter your four digit number"))
    r = 0

    r = r + num%10
    num = num//10

    r = r + num%10
    num = num//10

    r = r + num%10
    num = num//10

    r = r + num%10
    num = num//10

    print("The sum of digit of number ",r)





def function5th():
    MP = int(input("Enter your premium in multiples of 5"))
    fives = MP//5
    Maturity=fives*365.27
    print(f"the maturiy is {Maturity} ")







def function6th():
    sale=int(input("inter your sale"))
    cost=int(input("inter your cost"))


    if cost - sale > 0:
         profit = cost - sale
         print("Profit is",profit)
    if sale-cost > 0:
        loss = sale -cost
        print("loss is",loss)






def function7th():
    KM = int(input("Enter distance in km"))

    metre = KM*1000

    feet = KM*3281

    cm = KM*100000

    inch= KM*39370

    print("Km in metre is ", metre)
    print("km in feet is ",feet)
    print("km in inches is ",inch)
    print("km in cm is ",cm)







def function8th():
    F=int(input("Enter your temperature in fahrenheit"))

    celcius = (F-32)*5/9

    print(f"The temperature in celcius is {celcius}")






def function9th():
    num=int(input("enter your one number"))

    if num%2==0:
        print("number is even")

    else:
        print("number is odd")
    
    





    





