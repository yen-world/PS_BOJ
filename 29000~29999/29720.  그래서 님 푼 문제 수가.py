n, m, k = map(int, input().split())

min_ploblem = n - m * k
max_plobelm = min_ploblem + m - 1

if min_ploblem < 0:
    min_ploblem = 0
if max_plobelm < 0:
    max_plobelm = 0

print(min_ploblem, max_plobelm)
