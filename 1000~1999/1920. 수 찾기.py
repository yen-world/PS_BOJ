import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

for i in range(M):
    mid = len(A) // 2
    start = 0
    end = len(A) - 1
    while True:
        if start <= end:
            if A[mid] == B[i]:
                B[i] = 1
                break
            elif A[mid] > B[i]:
                end = mid - 1
                mid = (start + end) // 2
            elif A[mid] < B[i]:
                start = mid+1
                mid = (start + end) // 2
        else:
            B[i] = 0
            break

for i in B:
    print(i)
