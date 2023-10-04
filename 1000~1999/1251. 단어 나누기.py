word = input()
temp = []
result = '{'

for i in range(1, len(word)-1) :
    for j in range(i+1, len(word)) :
        temp = ''.join(list(reversed(word[:i])) + list(reversed(word[i:j])) + list(reversed(word[j:])))
        if result > temp :
            result = temp

print(result)