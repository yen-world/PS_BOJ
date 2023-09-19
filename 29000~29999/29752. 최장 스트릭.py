n = int(input())
solve = list(map(int, input().split()))
now_streak = 0
max_streak = 0

for i in range(len(solve)):
    if solve[i] > 0:
        now_streak += 1
    else:
        if max_streak < now_streak:
            max_streak = now_streak
        now_streak = 0

print(max(now_streak, max_streak))
