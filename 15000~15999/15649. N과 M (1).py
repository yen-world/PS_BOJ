# from itertools import permutations

# n, m = map(int, input().split())
# permutation = list(permutations(range(1, n + 1), m))

# for items in permutation:
#     for item in items:
#         print(item, end=" ")
#     print()


n, m = map(int, input().split())
result = []


def dfs():
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n + 1):
        if i in result:
            continue
        result.append(i)
        dfs()
        result.pop()


dfs()
