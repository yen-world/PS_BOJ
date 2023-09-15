import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
a = int(input())

result = 0

for i in range(m-a+1) :
    sum_value = 0
    for j in range(n) :
        sum_value += sum(matrix[j][i:i+a])
    if result < sum_value :
        result = sum_value

print(result)
