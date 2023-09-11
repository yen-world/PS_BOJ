matrix = [[0 for i in range(100)] for j in range(100)]

input_case = int(input())
count = 0

for i in range(input_case):
    width, height = map(int, input().split())
    height = 100 - height
    for i in range(10):
        for j in range(10):
            if matrix[height-j][width+i] == 0:
                matrix[height-j][width+i] = 1

for i in matrix:
    count += i.count(1)
print(count)
