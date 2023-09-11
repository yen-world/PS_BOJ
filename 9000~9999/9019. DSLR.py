from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque([])
    queue.append([A, ''])
    visitied = [False for i in range(10000)]
    visitied[A] = True
    while queue:
        num, path = queue.popleft()
        visitied[num] = True
        if num == B:
            return path

        next_num = num * 2 % 10000
        if not visitied[next_num]:
            visitied[next_num] = True
            queue.append([next_num, path+'D'])

        next_num = (num-1) % 10000
        if not visitied[next_num]:
            visitied[next_num] = True
            queue.append([next_num, path+'S'])

        next_num = (num % 1000 * 10) + (num // 1000) % 10000
        if not visitied[next_num]:
            visitied[next_num] = True
            queue.append([next_num, path+'L'])

        next_num = (num // 10) + (num % 10 * 1000) % 10000
        if not visitied[next_num]:
            visitied[next_num] = True
            queue.append([next_num, path+'R'])


case = int(input())

for i in range(case):
    A, B = map(int, input().split())
    print(bfs())
