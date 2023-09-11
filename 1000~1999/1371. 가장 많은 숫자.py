dictionary = {}
sentence = []
result = []

while True:
    try:
        sentence.append(input())
    except EOFError:
        break

for line in sentence:
    for char in line:
        if dictionary.get(char) == None:
            dictionary[char] = 0
        dictionary[char] += 1

if dictionary.get(" ") != None:
    del dictionary[" "]

result = [k for k, v in dictionary.items() if max(dictionary.values()) == v]
result.sort()

for i in result:
    print(i, end="")
