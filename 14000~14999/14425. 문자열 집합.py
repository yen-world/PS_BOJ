import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = []
string_list = []

count = 0

for i in range(N):
    S.append(input().rstrip())

for i in range(M):
    string_list.append(input().rstrip())

for j in range(M):
    if string_list[j] in S:
        count += 1

print(count)
