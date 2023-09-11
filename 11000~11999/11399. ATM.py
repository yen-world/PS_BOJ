person = int(input())
weight = list(map(int, input().split()))
weight.sort()

result = 0

for i in range(len(weight)):
    for j in range(i+1):
        result += weight[j]

print(result)
