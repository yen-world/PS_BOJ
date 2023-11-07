n = int(input())
list = []
result = 0

for i in range(1, n - 1):
    for j in range(i, n - 1):
        k = n - i - j

        if k < j:
            break

        if k < i + j:
            result += 1

print(result)
