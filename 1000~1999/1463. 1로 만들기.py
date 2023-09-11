number = int(input())

dp = [1e9 for i in range(1000001)]
dp[1] = 0

for i in range(2, number+1):
    if i % 3 == 0 and dp[i] > 1 + dp[i//3]:
        dp[i] = 1 + dp[i//3]
    if i % 2 == 0 and dp[i] > 1 + dp[i//2]:
        dp[i] = 1 + dp[i//2]
    if i - 1 > 1 and dp[i] > 1 + dp[i-1]:
        dp[i] = 1 + dp[i-1]

print(dp[number])
