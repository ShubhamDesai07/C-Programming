num = int(input("enter any nummber"))


if num > 1 :
    for i in range(2,num):
        if num % i == 0 :
            print(f"{num}is not a prime " )
            break
    else:
        print(f"{num} is a prime ")
else:
    print(f"{num} is not a prime")        
      


      