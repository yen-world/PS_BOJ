import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    op = int(input())
    if op == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-op, op))
    print(heap)
