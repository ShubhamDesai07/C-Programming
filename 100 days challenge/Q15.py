#check entered number is positive or negative

num = int(input("Enter a number "))

if num>0:
    print(f"{num} is positive ")
elif  num<0:
    print(f"{num} is negative")
elif  num==0:
    print(f"{num} is zero it is niether negative nor positive")        