dp = [3]

for i in range(1, 15):
    dp.append(dp[i-1] * 2 - 1)

print(dp[int(input())-1] ** 2)
