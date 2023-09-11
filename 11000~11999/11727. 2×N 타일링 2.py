number = int(input())
dp = [0 for i in range(1000)]
dp[0] = 1
dp[1] = 3

for i in range(2, number):
    if dp[i] == 0:
        dp[i] = (dp[i-2]*2) + dp[i-1]

print(dp[number-1] % 10007)
