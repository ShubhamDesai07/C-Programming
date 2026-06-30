#to find greater number from entered two number

num1 = int(input("Enter a number"))
num2 = int (input("Enter a number "))
num3 = int (input("Enter a number "))

if num1 > num2 and num1>num3:
    print(f"{num1} is greater than {num2} and {num3}" )
elif  num1==num2==num3:
    print("All numbers are same")
elif num3>num2 and num3>num1:
    print(f"{num3} is greater than {num1} and {num2}")    

    
else:
    print(f"{num2} is greater than {num1} and {num3}")    