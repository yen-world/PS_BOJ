import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = []
result = 1e9

for i in range(N):
    ground.append(list(map(int, input().split())))

min_value = min(map(min, ground))
max_value = max(map(max, ground))

for i in range(min_value, max_value+1):
    add_block = 0
    remove_block = 0
    time = 0
    for j in range(N):
        for k in range(M):
            remo = ground[j]
            # 층수보다 높으면? 그만큼 빼야함(블럭 제거)
            if ground[j][k] > i:
                remove_block += ground[j][k] - i
            # 층수보다 낮으면? 그만큼 더해야함(블럭 추가)
            else:
                add_block += i - ground[j][k]
    if add_block <= remove_block + B:
        time = remove_block * 2 + add_block
        if time <= result:
            result = time
            level = i

print(result, level)
