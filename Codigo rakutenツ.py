S = input(b)
word = list(S)
dig_list = []


for i in range(0, len(word)):
    for j in range(i+1, len(word)):
        if (i+1 < len(word)) and (j+1 < len(word)):
            if (word[i] == word[j]) and (word[i+1] == word[j+1]):
                dig_list.append(j-i)

if len(dig_list) > 0:
    print(max(dig_list))
else:
    return -1