N = int(input())

students = dict()
list = list(map(int, input().split()))

result = 0

for i in range(N):
    if list[i] not in students:
        students[list[i]] = 0
    students[list[i]] += 1

    if students[list[i]] <= 2:
        result += 1

print(result)
