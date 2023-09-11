M = int(input())
N = int(input())
count = 0
list = []

for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                count += 1
                list.append(i)
            else:
                break

if len(list) == 0:
    print(-1)
else:
    print(sum(list))
    print(min(list))
