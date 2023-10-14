E, S, M = map(int, input().split())
t_E, t_S, t_M = 1, 1, 1
result = 1

while True :
    if t_M == M and t_S == S and t_E == E :
        print(result)
        break

    result += 1
    
    if t_E < 15 :
        t_E += 1
    else :
        t_E = 1

    if t_S < 28 :
        t_S += 1
    else :
        t_S = 1

    if t_M < 19 :
        t_M += 1
    else :
        t_M = 1