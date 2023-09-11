n, l, d = map(int, input().split())
flag = []
result = 0

# True: 노래를 듣는 시간
# False: 노래를 듣지 않는 시간
for i in range(n) :
    for j in range(l) :
        flag.append(True)
    if i != n-1:
        for j in range(5) :
            flag.append(False)

for i in range(0, len(flag), d) :
    if flag[i] == False :
        result = i
        break
else :
    result = i + d

print(result)