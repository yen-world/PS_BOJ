A, B = map(int, input().split())
m = int(input())
numbers = list(map(int, input().split()))
decimal = 0

for i in range(m):
    decimal += A ** (m - i - 1) * numbers[i]

result = []
exp = 0

while True:
    if decimal // B**exp < 1:
        count = exp - 1
        break
    exp += 1

for i in range(count, -1, -1):
    result.append(decimal // B**i)
    decimal %= B**i

print(*result)
