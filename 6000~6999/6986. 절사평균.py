import sys

input = sys.stdin.readline

n, k = map(int, input().split())
score = []

for i in range(n):
    score.append(float(input()))
score.sort()

if k != 0:
    avg1 = sum(score[k:-k]) / (n - k * 2)
    avg2 = sum(score[k:-k])
else:
    avg1 = sum(score) / (n - k * 2)
    avg2 = sum(score)

for i in range(k):
    avg2 += score[k]
    avg2 += score[-k - 1]
avg2 /= n

print("%.2f" % (avg1 + 1e-9))
print("%.2f" % (avg2 + 1e-9))
