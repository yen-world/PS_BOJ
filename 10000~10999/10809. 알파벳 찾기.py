word = input().lower()
list = [-1 for i in range(26)]
count = 1

for i in range(len(word)) :
    if(word[i] >= 'a' and word[i] <= 'z') :
        if (list[(ord(word[i])-97)] == -1) :
            list[(ord(word[i])-97)] += count
        count += 1

for i in range(len(list)) :
    print(list[i], end=' ')