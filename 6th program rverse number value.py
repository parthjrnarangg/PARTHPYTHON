num =int(input("Enter your four digit number"))

r= 0
x=num
r = r*10 + num%10
num = num//10

r = r*10 + num%10
num = num//10

r = r*10 + num%10
num = num//10

r = r*10 + num%10
num = num//10

if x==r:
    print("the number is panidrom")

else:
    print("the number is not panidrom")

    

                
