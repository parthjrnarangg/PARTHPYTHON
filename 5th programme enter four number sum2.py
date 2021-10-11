num = int(input("Enter your four digit number "))
r=0

r = r + num%10
num = num//10

r = r + num%10
num = num//10

r = r + num%10
num = num//10

r = r + num%10
num = num//10

print("the sum is ",r)





