str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("not anagram")
else:
    flag = True

    for ch in str1:
        count1 = 0
        count2 = 0
        for i in str1:
            if i == ch:
                count1 += 1
        for j in str2:
            if j == ch:
                count2 += 1
        if count1 != count2:
            flag = False
            break
if flag:
    print("anagram ")
else :
    print("not anagram")                                  