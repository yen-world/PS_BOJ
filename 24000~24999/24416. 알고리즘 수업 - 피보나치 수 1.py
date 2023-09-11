def fibonacci_dp(n):
    global count
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        count += 1
    return dp[n]


n = int(input())
count = 0
print(fibonacci_dp(n), count)
