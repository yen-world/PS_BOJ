# import math

# N, K = map(int, input().split())

# print(math.comb(N, K) % 10007)


# N, K = map(int, input().split())

# result = 1
# for i in range(N, N-K, -1):
#     result *= i

# for i in range(1, K+1):
#     result //= i

# print(result % 10007)

# 파스칼의 삼각형
n, k = map(int, input().split())
dp = [[0] * 1 for i in range(1002)]
dp[1].append(1)
for i in range(2, 1002):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
print(dp[n + 1][k + 1] % 10007)
