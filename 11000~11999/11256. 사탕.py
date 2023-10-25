import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    candy, N = map(int, input().split())
    box = []
    result = 0

    for j in range(N):
        R, C = map(int, input().split())
        box.append(R * C)
    box.sort(reverse=True)

    for i in range(1, N + 1):
        if sum(box[0:i]) >= candy:
            result = i
            break

    print(result)
