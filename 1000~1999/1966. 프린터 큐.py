case = int(input())

for i in range(case):
    document, position = map(int, input().split())
    queue = list(map(int, input().split()))
    count = 0

    for j in range(document):
        queue[j] = [queue[j], j]
    while queue:
        if queue[0][0] < max(queue)[0]:
            queue.append(queue.pop(0))
        else:
            if queue[0][1] == position:
                queue.pop(0)
                count += 1
                break
            else:
                queue.pop(0)
                count += 1
    print(count)
