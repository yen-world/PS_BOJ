import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for i in range(N) :
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for i in range(M) :
    B.append(list(map(int, input().split())))

result = []

for i in range(N) :
    temp = []
    for j in range(K) :
        value = 0
        for k in range(M) :
            value += A[i][k] * B[k][j]
        temp.append(value)
    result.append(temp)

for line in result :
    print(*line)