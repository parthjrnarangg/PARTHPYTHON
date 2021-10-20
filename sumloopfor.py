numbers=[55,64,74,85,42]
sum=0

for number in numbers:
    sum=sum+number

    print(number," + ",end="")

avg=sum/len(numbers)

print("\b\b = ",sum)

print("Average =",avg)
