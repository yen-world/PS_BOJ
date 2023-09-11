matrix = [[] for i in range(5)]

for i in range(5):
    string = input()
    for j in range(len(string)):
        matrix[i].append(string[j])

for i in range(15):
    for j in range(5):
        try:
            print(matrix[j][i], end='')
        except IndexError:
            continue
