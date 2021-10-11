year=int(input("enter your year"))


if year%400==0:
    print("year is leap year")

elif year%4==0 and year%100!=0:
    print("year is leap year")

else:
    print("invaild")
       
