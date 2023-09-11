n = int(input())
f = int(input())
temp = str(n)
temp = int(temp[-2:])
n -= temp

for i in range(n, n+101):
    if i % f == 0:
        result = i
        break

result = str(result)
print(result[-2:])
