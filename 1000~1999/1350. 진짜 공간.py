n = int(input())
files = list(map(int, input().split()))
cluster = int(input())
result = 0

for file in files:
    result += cluster * (file // cluster)
    if file % cluster != 0:
        result += cluster

print(result)
