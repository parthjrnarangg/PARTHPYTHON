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





