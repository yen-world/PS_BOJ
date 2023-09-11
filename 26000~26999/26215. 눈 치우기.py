import sys
input = sys.stdin.readline

n = int(input())
home = list(map(int, input().split()))
home.sort()
result = 0

while home:
    if len(home) >= 2:
        home[-1] -= 1
        home[-2] -= 1
        result += 1
    else:
        home[-1] -= 1
        result += 1
    if result > 1440:
        result = -1
        break
    home.sort()

    while home:
        if home[0] == 0:
            home.pop(0)
        else:
            break

print(result)
