#90+  → A
#70–89 → B
#50–69 → C
#<50 → Fail
#Enter marks: 82
#Grade: B

marks = int(input("Enter the marks : "))

if marks >= 90:
    print("GRADE A")
elif marks <= 89 and marks >= 70 :
    print("GRADE B ")
elif marks <= 69 and marks >= 50 :
    print("GRADE C")
else:
    print("FAIL")          
    