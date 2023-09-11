n = int(input())
candy = []

for i in range(n):
    candy.append(int(input()))
sum_value = sum(candy) // 2
result = [sum_value] * n

for i in range(n):
    for j in range(0, n-1, 2):
        result[i] -= candy[(i+j+1) % n]

for i in result:
    print(i)
