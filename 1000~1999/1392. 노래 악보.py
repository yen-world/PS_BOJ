n, q = map(int, input().split())
times = [int(input()) for i in range(n)]
quetions = [int(input()) for i in range(q)]

for i in range(len(quetions)) :
    target = quetions[i]
    sum_time = 0
    for j in range(len(times)) :
        sum_time += times[j]
        if target < sum_time :
            print(j+1)
            break