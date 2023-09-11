n = int(input())
result = 0
time, bird = 0, n

while bird != 0:
    time += 1
    if time <= bird:
        bird -= time
        result += 1
    else:
        time = 0

print(result)
