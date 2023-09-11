case = int(input())

for i in range(case):
    closet = {}
    clothes_count = int(input())
    kind_list = []
    result = 1
    for j in range(clothes_count):
        name, kind = list(map(str, input().split()))
        if kind not in kind_list:
            kind_list.append(kind)
        if kind not in closet:
            closet[kind] = 1
        else:
            closet[kind] += 1

    for j in range(len(kind_list)):
        result *= (closet[kind_list[j]] + 1)

    print(result-1)
