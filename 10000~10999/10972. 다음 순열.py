n = int(input())
permutation = list(map(int, input().split()))
result = []
curve_point = -1

for i in range(n - 1):
    if permutation[i] < permutation[i + 1]:
        curve_point = i

if curve_point == -1:
    print(curve_point)
    exit()

for i in range(curve_point, n):
    if permutation[curve_point] < permutation[i]:
        change_number = i

permutation[curve_point], permutation[change_number] = (
    permutation[change_number],
    permutation[curve_point],
)

temp_arary = list(reversed(permutation[curve_point + 1 :]))
result.extend(permutation[: curve_point + 1])
result.extend(temp_arary)

print(*result)
