a, b = map(int, input().split())
k, x = map(int, input().split())
result = 0

for i in range(a, b+1) :
    if k-x <= i <= k+x :
        result += 1

if result :
    print(result)
else :
    print("IMPOSSIBLE")