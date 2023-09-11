import sys

input_number = int(sys.stdin.readline())
num_list = []

for i in range(input_number):
    num_list.append(int(sys.stdin.readline()))

count_list = [0] * (max(num_list)+1)

for i in num_list:
    count_list[i] += 1

for i in range(max(num_list)):
    while count_list[i] != 0:
        num_list[i] = count_list.index(i+1)
        count_list[i] -= 1

print(num_list)
