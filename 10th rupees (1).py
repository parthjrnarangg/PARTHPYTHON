RS= int(input("Enter the rupees you want"))

hundreds = RS//100
RS = RS%100  
fifty = RS//50
RS = RS%50
twenty = RS//20
RS = RS%20
ten = RS//10
RS = RS%10
five = RS//5
RS = RS%5
two = RS//2
RS = RS%2
one = RS//1

print("hundreds",hundreds)
print("fifty",fifty)
print("twenty",twenty)
print("ten",ten)
print("five",five)
print("two",two)
print("one",one)



