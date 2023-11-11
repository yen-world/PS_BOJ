n = int(input())
max_list = []

for i in range(1, n + 1):
    temp_list = []
    temp_list.append(n)
    temp_list.append(i)
    count = 0

    while True:
        value = temp_list[count] - temp_list[count + 1]
        if value < 0:
            break

        temp_list.append(temp_list[count] - temp_list[count + 1])
        count += 1

    if len(temp_list) > len(max_list):
        max_list = temp_list.copy()


print(len(max_list))
print(*max_list)
