N = int(input())
score = 0
cont = 0

for i in range(N) :
    result = input()
    for j in range(len(result)) :
        if result[j] == 'O' :
            cont += 1
            score += cont
        else :
            cont = 0
    print(score)
    score = 0
    cont = 0