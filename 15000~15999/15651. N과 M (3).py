def dfs():
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n + 1):
        result.append(i)
        dfs()
        result.pop()


n, m = map(int, input().split())
result = []
dfs()
