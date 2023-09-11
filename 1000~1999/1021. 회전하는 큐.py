from collections import deque

N, M = map(int, input().split())
index_list = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
result = 0

for i in range(M):
    queue2 = deque(queue)
    queue3 = deque(queue)
    count2 = 0
    count3 = 0
    if queue[0] == index_list[i]:  # 1번 연산
        queue.popleft()
    else:
        while True:
            queue2.append(queue2.popleft())  # 2번 연산
            count2 += 1
            if queue2[0] == index_list[i]:
                break
        while True:
            queue3.appendleft(queue3.pop())  # 3번 연산
            count3 += 1
            if queue3[0] == index_list[i]:
                break
        if count2 > count3:
            while True:
                queue.appendleft(queue.pop())
                result += 1
                if queue[0] == index_list[i]:
                    queue.popleft()
                    break
        else:
            while True:
                queue.append(queue.popleft())
                result += 1
                if queue[0] == index_list[i]:
                    queue.popleft()
                    break

print(result)
