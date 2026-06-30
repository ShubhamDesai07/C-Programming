c = 1000
def add(a,b):
    if (a>5 or b<4):
        #global c
        c = 0 
        c = a + b 
        print("addition is ",c,"this is a local c")
    else:
        pass 
a = int(input("enter number"))
b = int (input("enter number"))
add(a,b)

print("global  C = ",c)