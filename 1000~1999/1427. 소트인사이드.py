input_ = input()

num_list = []
for i in range(len(input_)):
    num_list.append(input_[i])
num_list.sort(reverse=True)

for i in num_list:
    print(i, end='')
