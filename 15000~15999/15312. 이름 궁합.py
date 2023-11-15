A = input()
B = input()
name = ''
result = []
temp = []

stroke = {"A" : 3, "B" : 2, "C" : 1, "D" : 2, "E" : 3, "F" : 3, "G" : 2, 
          "H" : 3, "I" : 3, "J" : 2, "K" : 2, "L" : 1, "M" : 2, "N" : 2,
          "O" : 1, "P" : 2, "Q" : 2, "R" : 2, "S" : 1, "T" : 2, "U" : 1,
          "V" : 1, "W" : 1, "X" : 2, "Y" : 2, "Z" : 1}

for i in range(len(A)) :
    name += A[i]
    result.append(stroke[A[i]])
    name += B[i]
    result.append(stroke[B[i]])

for i in range(len(name) - 2):
    for j in range(len(result) - 1) :
        temp.append((result[j] + result[j+1]) % 10)
    result.clear()
    result.extend(temp)
    temp.clear()

for i in result :
    print(i, end='')