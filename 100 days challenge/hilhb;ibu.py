data = "apple"



count = {}

for char in data:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)