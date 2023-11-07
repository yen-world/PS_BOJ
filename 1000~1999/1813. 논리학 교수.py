N = int(input())
numbers = list(map(int, input().split()))

result = -1

for i in range(N + 1):
    true_count = numbers.count(i)

    if true_count == i:
        result = max(result, i)

print(result)
