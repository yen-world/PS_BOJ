cost = int(input())
kind = int(input())
result = 0
for i in range(kind) :
    price, count = map(int, input().split())
    result += price * count

if (cost == result) :
    print("Yes")
else :
    print("No")