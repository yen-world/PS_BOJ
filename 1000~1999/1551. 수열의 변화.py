n, k = map(int, input().split())
n_list = list(map(int, input().split(",")))

for i in range(k):
    temp = []
    for j in range(len(n_list) - 1):
        temp.append(n_list[j + 1] - n_list[j])
    n_list.clear()
    n_list.extend(temp)

print(",".join(map(str, n_list)))
