matrix = []

for i in range(15):
    matrix.append(list(map(str, input().split())))

for i in range(15):
    for j in range(15):
        if matrix[i][j] == "w":
            print("chunbae")
            exit()
        if matrix[i][j] == "b":
            print("nabi")
            exit()
        if matrix[i][j] == "g":
            print("yeongcheol")
            exit()
