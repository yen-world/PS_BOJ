N, m, M, T, R = map(int, input().split())
X = m
workout_time = 0
total_time = 0

while workout_time < N:
    if X + T <= M:
        X += T
        workout_time += 1
        total_time += 1
    elif X + T > M:
        if X - R >= m:
            X -= R
            total_time += 1
        else:
            X = m
            total_time += 1
    if M - m < T:
        total_time = -1
        break
print(total_time)
