import sys
input = sys.stdin.readline

N, M = map(int, input().split())

person = {}
count = 0
result = []

for i in range(N):
    person[input().rstrip()] = 0

for i in range(M):
    name = input().rstrip()
    if name in person:
        result.append(name)
        count += 1

print(count)
result.sort()
for i in result:
    print(i)
