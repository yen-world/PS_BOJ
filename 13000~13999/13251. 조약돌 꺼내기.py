m = int(input())
colors = list(map(int, input().split()))
k = int(input())
n = sum(colors)
result = 0.0

for i in range(m):
    left_ball = n
    ball = colors[i]
    temp = 1
    for j in range(k):
        temp *= ball / left_ball
        ball -= 1
        left_ball -= 1
    result += temp

print(result)
