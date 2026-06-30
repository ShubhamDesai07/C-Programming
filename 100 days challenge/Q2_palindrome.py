string = input("Enter a string :")
reverse = ""

for ch in string:
    reverse = ch + reverse
if string == reverse:
    print("palindrome string")
else:
    print("not palindrome string")