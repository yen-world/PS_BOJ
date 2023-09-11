n, m, l = map(int, input().split())
li = [0 for i in range(n)]
idx = 0
li[idx] += 1

count = 0

while True:
    if li[idx] == m:
        print(count)
        break

    count += 1
    if li[idx] % 2 == 0:
        idx = (idx + l) % n
        li[idx] += 1
    else:
        idx = (idx - l) % n
        li[idx] += 1
