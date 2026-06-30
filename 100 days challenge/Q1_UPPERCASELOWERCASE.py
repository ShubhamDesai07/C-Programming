name = "AniSh"

uppercase = 0
lowercase = 0

for ch in name:
    if ch >='A' and ch <='Z':
        uppercase += 1 
    elif ch >='a' and ch <='z':
        lowercase += 1 

print ("uppercase letters:",uppercase) 
print ("lowercase letters :",lowercase)
