score = []
temp = []
result = []

for i in range(8):
    n = int(input())
    score.append(n)
    temp.append(n)

score.sort()

for i in range(7, 2, -1):
    result.append(temp.index(score[i]) + 1)

result.sort()

print(sum(score[3:8]))
print(*result)
