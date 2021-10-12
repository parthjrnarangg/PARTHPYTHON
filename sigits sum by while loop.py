num = int(input("enter your four digit number"))
r = 0
while num>0:
    r = r + num%10
    num = num//10
print("Sum is",r)


