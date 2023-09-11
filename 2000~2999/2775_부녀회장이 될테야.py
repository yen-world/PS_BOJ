test_case = int(input())
result = 0

for i in range(test_case):
    floor = int(input())
    room = int(input())

    apartment = [[0 for row in range(1, room+1)] for col in range(floor)]

    for i in range(room):
        apartment[0][i] = i+1

    for i in range(1, floor):
        for j in range(room):
            for k in range(j+1):
                apartment[i][j] += apartment[i-1][k]

    for i in range(room):
        result += apartment[floor-1][i]

    print(result)

    result = 0
