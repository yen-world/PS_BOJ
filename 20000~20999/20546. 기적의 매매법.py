cash = int(input())
stock = list(map(int, input().split()))

jh_cash = cash
jh_stock = 0

for i in range(14):
    if stock[i] <= jh_cash:
        jh_stock += jh_cash // stock[i]
        buy_stock = jh_cash // stock[i] * stock[i]
        jh_cash = jh_cash - buy_stock

sm_cash = cash
sm_stock = 0
increase_count = 0
decrease_count = 0

for i in range(1, 14):
    if stock[i - 1] < stock[i]:  # 증가하는 경우
        increase_count += 1
        decrease_count = 0
    elif stock[i - 1] > stock[i]:  # 감소하는 경우
        decrease_count += 1
        increase_count = 0
    else:  # 같은 경우
        increase_count = 0
        decrease_count = 0

    if decrease_count >= 3:  # 3일 연속 하락의 경우 매수
        if stock[i] <= sm_cash:
            sm_stock += sm_cash // stock[i]
            buy_stock = sm_cash // stock[i] * stock[i]
            sm_cash = sm_cash - buy_stock
    elif increase_count >= 3:  # 3일 연속 상승의 경우 매도
        sm_cash += stock[i] * sm_stock
        sm_stock = 0

jh_total_cash = jh_cash + jh_stock * stock[-1]
sm_total_cash = sm_cash + sm_stock * stock[-1]

if jh_total_cash > sm_total_cash:
    print("BNP")
elif jh_total_cash < sm_total_cash:
    print("TIMING")
else:
    print("SAMESAME")
