T = int(input())

for i in range(T) :
    letter = input()
    matrix = []
    length = int(len(letter) ** 0.5)
    result = ''

    for j in range(length) : 
        matrix.append(letter[j*length:(j+1)*length])

    for j in range(length-1, -1, -1) :
        for k in range(length) :
            result += matrix[k][j]
    
    print(result)