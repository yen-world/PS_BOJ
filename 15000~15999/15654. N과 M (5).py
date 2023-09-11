# from itertools import permutations
# n, m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# result = list(permutations(n_list, m))

# for i in result :
#     for j in i :
#         print(j, end=' ')
#     print()

def dfs(depth) :
    if depth == m :
        print(*result)
        return
    else :
        for i in range(n) :
            if not visited[i] : 
                result.append(n_list[i])
                visited[i] = True
                dfs(depth+1)
                visited[i] = False
                result.pop() 


n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
result = []
visited = [False] * n

dfs(0)