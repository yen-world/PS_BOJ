import sys
input = sys.stdin.readline

n, c = map(int, input().split())
time = [False for i in range(c)]

for i in range(n) :
    bomb = int(input())
    for j in range(bomb, c+1, bomb) :
        if time[j-1] == False :
            time[j-1] = True

print(time.count(True))
