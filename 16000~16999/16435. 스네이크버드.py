N, L = map(int, input().split())
height = list(map(int, input().split()))
height.sort()

for i in height:
    if L >= i:
        L += 1
    else:
        break

print(L)
