n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
students = [0] * n

for i in range(n) :
    flag = [False] * n
    for j in range(5) :
        for k in range(n) :
            if i != k and matrix[i][j] == matrix[k][j]:
                flag[k] = True
    students[i] = flag.count(True)

print(students.index(max(students)) + 1)