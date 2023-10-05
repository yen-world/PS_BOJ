S = int(input())
count = 0
sum_value = 0

for i in range(1, 4294967296):
    sum_value += i
    if sum_value > S:
        break
    count += 1

print(count)
