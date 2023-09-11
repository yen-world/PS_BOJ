import sys

input_case = int(sys.stdin.readline())
data = []
for i in range(input_case):
    data.append(int(sys.stdin.readline()))
sorted_data = sorted(data)
for i in range(input_case):
    print(sorted_data[i])
