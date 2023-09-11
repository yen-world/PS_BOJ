def dfs():
    if len(result) == m:
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                break
        else:
            print(*result)
        return

    for i in range(1, n + 1):
        if i in result:
            continue
        result.append(i)
        dfs()
        result.pop()


n, m = map(int, input().split())
result = []
dfs()
