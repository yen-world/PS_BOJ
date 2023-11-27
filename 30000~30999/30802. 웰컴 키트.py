import math

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

shirt, pens, pen = 0, 0, 0

for i in range(6):
    shirt += math.ceil(size[i] / T)

pens = N // P
pen = N % P

print(shirt)
print(pens, pen)
