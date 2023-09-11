t = int(input())

for i in range(t):
    n = int(input())
    mbti = list(map(str, input().split()))
    if n >= 33:
        print(0)
    else:
        result = 10000
        for i in range(len(mbti)):
            for j in range(i + 1, len(mbti)):
                for k in range(j + 1, len(mbti)):
                    distance = 0
                    for l in range(4):
                        if mbti[i][l] != mbti[j][l]:
                            distance += 1
                        if mbti[j][l] != mbti[k][l]:
                            distance += 1
                        if mbti[i][l] != mbti[k][l]:
                            distance += 1
                    result = min(result, distance)

        print(result)
