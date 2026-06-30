#take input marks >75 First class with distinction ,60 to 70 First class , 50 to 60 second class,40 to 50 third class , below 40 fail



marks = int(input("Enter the marks"))

if marks>= 75 :
    print("First class with distinction")
elif marks >= 60:
    print("first class")
elif marks >= 50:
    print("second class")
elif marks >=40:
    print("third class")
else :
    print("Fail")            
        