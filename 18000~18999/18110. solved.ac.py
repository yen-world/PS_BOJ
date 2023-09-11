import sys
input = sys.stdin.readline

def round_(num):
    if num - int(num) >= 0.5 : return int(num) + 1
    else : return int(num)

n = int(input())
if n == 0 :
    print(0)
else :
    score = [int(input()) for i in range(n)]
    score.sort()
    rate = round_(n*0.15)

    slice_score = score[rate:n-rate]
    result = sum(slice_score) / (n - rate * 2)
    print(round_(result))