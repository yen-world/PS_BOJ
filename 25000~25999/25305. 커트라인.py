person, cut_line = map(int, input().split())
score = list(map(int, input().split()))

for i in range(len(score)):
    min_value = score[i]
    min_index = i
    for j in range(i, len(score)):
        if min_value > score[j]:
            min_value = score[j]
            min_index = j
    score[i], score[min_index] = score[min_index], score[i]

print(score[person-cut_line])
