case = int(input())
for i in range(case):
    quarter, dime, nickel, penny = 0, 0, 0, 0
    money = int(input())
    while money > 0:
        if money >= 25:
            quarter += 1
            money -= 25
        elif money >= 10:
            dime += 1
            money -= 10
        elif money >= 5:
            nickel += 1
            money -= 5
        elif money >= 1:
            penny += 1
            money -= 1
    print(quarter, dime, nickel, penny)
