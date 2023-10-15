K = int(input())

A = [0] * 46
B = [0] * 46

A[0], A[1] = 1, 0
B[0], B[1] = 0, 1

for i in range(2, 46):
    A[i] = A[i - 1] + A[i - 2]
    B[i] = B[i - 1] + B[i - 2]

print(A[K], B[K])
