# from itertools import combinations_with_replacement

# n, m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# result = list(combinations_with_replacement(n_list, m))

# for i in result :
#     for j in i :
#         print(j, end=' ')
#     print()

def dfs(depth) :
    if depth == m :
        for i in range(1, m+1) :
            print(result[i], end=' ')
        print()
        return
    else :
        for i in range(n) :
            if result[-1] <= n_list[i] :
                result.append(n_list[i])
                dfs(depth+1)
                result.pop()


n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
result = [0]
visited = [False] * n

dfs(0)