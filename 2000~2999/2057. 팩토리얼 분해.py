import math

n = int(input())
factorial = []
result = 0

for i in range(20):
    factorial.append(math.factorial(i))
factorial.reverse()

for i in factorial:
    if i <= n - result:
        result += i

if n == result:
    if n != 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
