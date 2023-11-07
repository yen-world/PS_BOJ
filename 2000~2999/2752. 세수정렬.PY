A, B, C = map(int, input().split())

max_value = max(A, B, C)
min_value = min(A, B, C)

if A == max_value and B == min_value:
    mid_value = C
elif A == max_value and C == min_value:
    mid_value = B
elif B == max_value and A == min_value:
    mid_value = C
elif B == max_value and C == min_value:
    mid_value = A
elif C == max_value and A == min_value:
    mid_value = B
elif C == max_value and B == min_value:
    mid_value = A

print(min_value, mid_value, max_value)
