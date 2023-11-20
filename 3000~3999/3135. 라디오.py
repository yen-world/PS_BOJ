A, B = map(int, input().split())
N = int(input())
frequency = []
AtoB = abs(A - B)
result = AtoB

for i in range(N):
    frequency.append(int(input()))
    if abs(frequency[i] - B) < result:
        result = abs(frequency[i] - B) + 1

print(result)
