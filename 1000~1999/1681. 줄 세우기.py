n, l = input().split()
n = int(n)
result = "0"
i = 1

while i <= n:
    result = int(result)
    result += 1
    result = str(result)
    if l not in result:
        i += 1

print(result)
