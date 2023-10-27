N = int(input())

for i in range(N, 0, -1) :
    i = str(i)
    for j in i :
        if j == '4' or j == '7' :
            continue
        else :
            break
    else :
        print(int(i))
        break