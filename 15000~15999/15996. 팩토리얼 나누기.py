from math import factorial

n, a = map(int, input().split())
k = 0

while True:
    if factorial(n) % a**k == 0:
        result = k

    if factorial(n) < a**k:
        break

    k += 1

print(result)
