import sys
import heapq
input = sys.stdin.readline

case = int(input())

for i in range(case):
    op = int(input())
    max_heap = []
    min_heap = []
    flag = [False] * 1000000
    for j in range(op):
        command, number = input().split()
        number = int(number)
        # 삽입 연산
        if command == 'I':
            heapq.heappush(max_heap, (-number, j))
            heapq.heappush(min_heap, (number, j))
            flag[j] = True
        # 최대 값 삭제 연산
        elif number == 1:
            while max_heap and not flag[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                flag[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        # 최소 값 삭제 연산
        else:
            while min_heap and not flag[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                flag[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    while max_heap and not flag[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not flag[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap and min_heap:
        print("{} {}".format(-max_heap[0][0], min_heap[0][0]))
    else:
        print("EMPTY")
