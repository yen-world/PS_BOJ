import sys
input = sys.stdin.readline

n = int(input())  # 이동하려는 채널
m = int(input())  # 고장난 버튼 갯수
button = list(map(str, input().split()))  # 고장난 버튼
result = abs(100-n)

for i in range(1000001):
    for j in str(i):
        if j in button:
            break
    else:
        result = min(result, len(str(i))+abs(i-n))

print(result)
