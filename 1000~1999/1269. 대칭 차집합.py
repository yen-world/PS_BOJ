import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A_set = ()
B_set = ()

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

A_diff = A_set-B_set
B_diff = B_set-A_set

result = len(A_diff) + len(B_diff)
print(result)
