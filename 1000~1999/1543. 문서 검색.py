document = input()
word = input()
result = 0
index = 0

while index < len(document) :
    if document[index:len(word)+index] == word :
        result += 1
        index += len(word)
    else :
        index += 1

print(result)