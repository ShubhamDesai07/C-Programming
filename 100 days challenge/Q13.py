#check enetered character is vowel or NOT

char = input("Enter the character")

''
#if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char ==  "U" :
if char in 'aeiouAEIOU':
    
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")    