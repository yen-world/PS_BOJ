import sys
input = sys.stdin.readline


def get_gcd(A, B):
    if A % B == 0:
        return B
    else:
        return get_gcd(B, A % B)


N = int(input())
trees = []
interval = []
count = 0

for i in range(N):
    trees.append(int(input()))
trees.sort()

for i in range(1, N):
    interval.append(trees[i]-trees[i-1])

gcd = interval[0]
for i in range(len(interval)):
    gcd = get_gcd(max(gcd, interval[i]), min(gcd, interval[i]))

print((trees[-1]-trees[0])//gcd-len(trees)+1)
