import heapq
import sys
input = sys.stdin.readline

heap = []

for i in range(int(input())):
    number = int(input())
    # 양수
    if number > 0:
        heapq.heappush(heap, (number, number))
        # 음수
    elif number < 0:
        heapq.heappush(heap, (-number, number))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
