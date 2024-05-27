from collections import deque


def BFS():
    queue = deque()
    queue.append(N)
    visited[N] = True
    dp[N] = 0

    while queue:
        value = queue.popleft()
        if 0 <= value - 1 <= 100000 and not visited[value - 1]:
            dp[value - 1] = dp[value] + 1
            visited[value - 1] = True
            queue.append(value - 1)
        elif 0 <= value - 1 <= 100000 and visited[value - 1]:
            dp[value - 1] = min(dp[value - 1], dp[value] + 1)

        if 0 <= value + 1 <= 100000 and not visited[value + 1]:
            dp[value + 1] = dp[value] + 1
            visited[value + 1] = True
            queue.append(value + 1)
        elif 0 <= value + 1 <= 100000 and visited[value + 1]:
            dp[value + 1] = min(dp[value + 1], dp[value] + 1)

        if 0 <= value * 2 <= 100000 and not visited[value * 2]:
            dp[value * 2] = dp[value]
            visited[value * 2] = True
            queue.append(value * 2)
        elif 0 <= value * 2 <= 100000 and visited[value * 2]:
            dp[value * 2] = min(dp[value * 2], dp[value])


N, K = map(int, input().split())
dp = [0] * 100001
visited = [False] * 100001

BFS()
print(dp[K])
