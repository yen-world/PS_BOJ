n = int(input())
counseling = [list(map(int, input().split())) for i in range(n)]
dp = [0 for i in range(n+1)]

for i in range(n-1, -1, -1):
    # 상담 진행일수가 퇴사일보다 길다면 상담을 진행 할 수 없음
    if i + counseling[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # 상담을 진행하지 않는것과, 상담을 진행하는 것 중 가장 큰 것을 고름
        dp[i] = max(dp[i+1], counseling[i][1] + dp[i + counseling[i][0]])
print(dp[0])
