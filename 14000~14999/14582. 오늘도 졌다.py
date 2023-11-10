a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = 0
b_score = 0

flag = False
result = False
for i in range(9):
    a_score += a[i]
    if a_score > b_score:
        flag = True
    else:
        flag = False

    b_score += b[i]
    if a_score < b_score:
        if flag:
            result = True

if result:
    print("Yes")
else:
    print("No")
