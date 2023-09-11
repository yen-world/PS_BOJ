N = int(input())
sum = 0.0

score = list(map(int, input().split()))
max = max(score)

for i in range(N) :
    score[i] = score[i] / max * 100
    sum += score[i]
    
print(sum / N)