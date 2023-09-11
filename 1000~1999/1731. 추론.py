n = int(input())
permutation = [int(input()) for _ in range(n)]

if permutation[1] * 2 == permutation[0] + permutation[2]:
    print(permutation[-1] + permutation[1] - permutation[0])
else:
    print(permutation[-1] * (permutation[1] // permutation[0]))
