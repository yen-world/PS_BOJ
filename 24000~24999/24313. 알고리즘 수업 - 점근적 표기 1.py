a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
flag = True
for i in range(n0, 100):
    if a1*i + a0 <= c * i:
        flag = True
        continue
    else:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)
