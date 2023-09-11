n = int(input())

dp = [0] * 1000001
dp[0] = 0
dp[1] = 1

for i in range(2, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000

if n > 0:
    print(1)
    print(dp[n])
elif n < 0:
    if n % 2 == 0:
        print(-1)
        print(dp[abs(n)])
    else:
        print(1)
        print(dp[abs(n)])
else:
    print(0)
    print(dp[n])
