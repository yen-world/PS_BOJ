A, B = input().split()
A_list = []
B_list = []
result = 0

for i in A:
    A_list.append(i)
for i in B:
    B_list.append(i)

for i in range(len(A_list)):
    for j in range(len(B_list)):
        result += int(A_list[i]) * int(B_list[j])

print(result)
