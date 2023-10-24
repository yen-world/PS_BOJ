H, W = map(int, input().split())
cloud = []
matrix = [[-1] * W for i in range(H)]
count = 0

for i in range(H):
    temp = []
    line = input()
    for j in range(W):
        temp.append(line[j])
    cloud.append(temp)

for k in range(W):
    for i in range(H):
        for j in range(W):
            if cloud[i][j] == "c" and matrix[i][j] == -1:
                matrix[i][j] = count

    for i in range(H):
        for j in range(W - 1, -1, -1):
            if cloud[i][j] == "c":
                if j == W - 1:
                    cloud[i][j] = "."
                else:
                    cloud[i][j] = "."
                    cloud[i][j + 1] = "c"
    count += 1

for line in matrix:
    print(*line)
