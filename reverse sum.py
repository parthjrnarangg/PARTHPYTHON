num =int(input("Enter your four digit number"))

r= 0
while num>0:
    r = r*10 + num%10
    num = num//10

print("THe revise number is",r)
