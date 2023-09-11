dice1, dice2, dice3 = map(int, input().split())

if (dice1 == dice2 and dice1 == dice3) : # 주사위 세개가 같은 경우
    print(10000 + (dice1 * 1000))
elif (dice1 == dice2) : # 주사위 1, 2가 같은 경우
    print(1000 + (dice1 * 100))
elif (dice1 == dice3) : # 주사위 1, 3가 같은 경우
    print(1000 + (dice1 * 100))
elif (dice2 == dice3) : # 주사위 2, 3가 같은 경우
    print(1000 + (dice2 * 100))
elif (dice1 != dice2 and dice1 != dice3) :
    print(max(dice1, dice2, dice3) * 100)