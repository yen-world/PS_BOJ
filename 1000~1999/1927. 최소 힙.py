import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    op = int(input())
    if op == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, op)
