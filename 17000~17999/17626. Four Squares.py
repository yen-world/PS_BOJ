nubmer = int(input())

dp = [1e9 for i in range(50001)]
dp[0] = 0
dp[1] = 1

for i in range(2, len(dp)):
    square = int(i ** (1/2))
    for j in range(1, square+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[nubmer])
