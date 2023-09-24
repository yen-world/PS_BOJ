import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
result = []
cnt = 0

for i in range(N - 1, -1, -1):
    if A[i] == 0 and cnt < M:
        result.append(B[i])
        cnt += 1

for i in range(M - len(result)):
    result.append(C[i])

print(*result)
