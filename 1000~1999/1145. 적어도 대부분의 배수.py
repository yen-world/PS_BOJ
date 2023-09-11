numbers = list(map(int, input().split()))

result = 0
count = 0
flag = False

while not flag:
    count = 0
    result += 1
    for i in range(5):
        if result % numbers[i] == 0:
            count += 1
        if count >= 3:
            flag = True

print(result)
