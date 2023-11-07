n, k = map(int, input().split())
pascal = [[], [1]]

for i in range(2, n + 1):
    pascal.append([])
    for j in range(i):
        if j == 0 or j == i - 1:
            pascal[i].append(1)
        else:
            pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])

print(pascal[n][k - 1])
