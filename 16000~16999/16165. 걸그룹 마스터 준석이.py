n, m = map(int, input().split())
girl_group = {}

for i in range(n):
    group_name = input()
    members = int(input())
    group = []
    for j in range(members):
        group.append(input())
    group.sort()
    girl_group[group_name] = group

for i in range(m):
    question = input()
    flag = int(input())
    if flag == 0:
        for member in girl_group[question]:
            print(member)
    else:
        for group in girl_group:
            if question in girl_group[group]:
                print(group)
