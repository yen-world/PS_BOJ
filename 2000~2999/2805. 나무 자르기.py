import sys
input = sys.stdin.readline

trees, need = map(int, input().split())
trees = list(map(int, input().split()))
most_height_tree = max(trees)
start = 0
end = most_height_tree
mid = (start + end) // 2
result = 0

while True:
    for i in trees:
        if i <= mid:
            continue
        else:
            result += i - mid

    if start <= end:
        if result < need:
            end = mid - 1
            mid = (start + end) // 2
            result = 0
        elif result >= need:
            start = mid + 1
            mid = (start + end) // 2
            result = 0
    else:
        break
print(mid)
