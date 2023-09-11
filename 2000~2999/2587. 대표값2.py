num_list = []
for i in range(5):
    num_list.append(int(input()))

for i in range(len(num_list)):
    min = num_list[i]
    min_index = i
    for j in range(i, len(num_list)):
        if min > num_list[j]:
            min = num_list[j]
            min_index = j
    num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

print(int(sum(num_list)/5))
print(num_list[5//2])
