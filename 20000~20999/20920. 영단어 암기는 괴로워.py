import sys
input = sys.stdin.readline

N, M = map(int, input().split())
count_list = []
dict = {}

for i in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    count_list.append(word)

for i in range(len(count_list)):
    if count_list[i] not in dict:
        dict[count_list[i]] = 0
        dict[count_list[i]] = dict[count_list[i]]+1
    else:
        dict[count_list[i]] = dict[count_list[i]]+1

sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in sorted_dict:
    print(i[0])
