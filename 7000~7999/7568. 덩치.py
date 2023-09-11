person = int(input())
info = []
ranking_list = []
ranking = 1

for i in range(person):
    info.append(list(map(int, input().split())))

for i in range(person):
    for j in range(person):
        if info[i][0] < info[j][0]:
            if info[i][1] < info[j][1]:
                ranking += 1
    ranking_list.append(ranking)

    ranking = 1

for i in ranking_list:
    print(i, end=' ')
