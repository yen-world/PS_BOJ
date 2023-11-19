def heap_sort(A):
    global count
    build_min_heap(A, N)
    for i in range(N, 1, -1):
        A[1], A[i] = A[i], A[1]
        count += 1
        if count == K:
            print(*A[1:])
            exit()
        heapify(A, 1, i - 1)


def build_min_heap(A, N):
    for i in range(N // 2, 0, -1):
        heapify(A, i, N)


def heapify(A, k, N):
    global count
    left = 2 * k
    right = 2 * k + 1
    if right <= N:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= N:
        smaller = left
    else:
        return

    if A[smaller] < A[k]:
        A[k], A[smaller] = A[smaller], A[k]
        count += 1
        if count == K:
            print(*A[1:])
            exit()
        heapify(A, smaller, N)


N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
count = 0

heap_sort(A)

print(-1)
