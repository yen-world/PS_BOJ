a, b = map(int, input().split())
result = 0

a -= 2
b -= 1
result += 3

while True:
    if a <= 0 or b <= 0:
        break
    else:
        a -= 1
        b -= 1
        result += 2

print(result)
