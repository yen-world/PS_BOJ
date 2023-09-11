A, B, C = map(int, input().split())
if max(A, B, C) == A:
    print(max(B, C))
elif max(A, B, C) == B:
    print(max(A, C))
else:
    print(max(A, B))
