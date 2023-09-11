C = int(input())
count = 0

for i in range(C):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    for j in range(1, len(score)):
        if avg < score[j]:
            count += 1
    print("%.3f%%" % (count / score[0] * 100))
    count = 0
