import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))
num_list.sort()

mean = round(sum(num_list) / N)  # 산술평균
print(mean)

median = num_list[N//2]  # 중앙값
print(median)

count = Counter(num_list).most_common()  # 최빈값
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

if N != 1:  # 범위
    range_ = num_list[-1] - num_list[0]
else:
    range_ = 0
print(range_)
