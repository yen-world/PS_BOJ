word = input().upper()
alphabet_list = [0 for i in range(26)]
max = -1
count = False

for i in range(len(word)) :
    alphabet_list[ord(word[i])-65] += 1
    
for i in range(len(alphabet_list)) :
    if (alphabet_list[max] < alphabet_list[i]) :
        max = i
        count = False
    elif (alphabet_list[max] == alphabet_list[i]) :
        if (i == 25) :
            max = 25
            break
        else :
            count = True
        
if (count) :
    print("?")
else :
    print(chr(max+65))