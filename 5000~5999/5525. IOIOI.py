N = int(input())
M = int(input())
S = input()
index = 0
count = 0
result = 0

while index < M:
    if S[index:index+3] == 'IOI':
        index += 2
        count += 1
        if count == N:
            result += 1
            count -= 1
    else:
        index += 1
        count = 0

print(result)
