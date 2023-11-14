import sys
input = sys.stdin.readline

X, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0

count = [0] * 10001

for i in range(X, 2 * X) :
    count[A[i]] += 1

for i in range(X) :
    result += X - count[A[i]]

print(result)