n = int(input())
students = [list(input().split()) for _ in range(n)]

max_list = []
min_list = []

for i in range(n):
    for j in range(1, 4):
        students[i][j] = int(students[i][j])

students.sort(key=lambda x: (-x[3], -x[2], -x[1]))

print(students[0][0], students[-1][0])
