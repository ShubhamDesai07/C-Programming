text = "apple"

count={}

for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1

print(count)      


text1 = "apple"
for char in set(text1):
    print(char,":",text1.count(char))
