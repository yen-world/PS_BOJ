K = int(input())

for i in range(K):
    info = list(map(int, input().split()))
    score = sorted(info[1:])
    gap = 0
    for j in range(len(score) - 1):
        if score[j + 1] - score[j] > gap:
            gap = score[j + 1] - score[j]
    print("Class {}".format(i + 1))
    print("Max {}, Min {}, Largest gap {}".format(max(score), min(score), gap))
