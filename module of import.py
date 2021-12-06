from funlib import*

choice = 1

while choice !=6:
    print("enter 1 for simple interest")
    print("enter 2 for interchange")
    print("enter 3 for net salary")
    print("enter 4 for sum of four digit number")
    print("enter 5 for maturity")
    print("enter 6 for exit")


    choice = int(input("ENTER THE PROGRAM NUMBER YOU WANT TO RUN"))

    if choice == 1 :
        function1st()

    elif choice == 2:
        function2nd()

    elif choice == 3:
        function3rd()

    elif choice == 4:
        function4th()

    elif choice == 5:
        function5th()

    elif choice == 6:
        break;
    else:
        print("INVALID INPUT ")
    
 

