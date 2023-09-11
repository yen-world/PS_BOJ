# 2019/01/01 화요일
# 2019/01/04 금요일

n = int(input())
day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
current_year, current_month, current_day = 2019, 1, 4
result = 0

while True :
    if current_year == n+1 :
        break

    if (current_year % 400 == 0) or (current_year % 100 != 0 and current_year % 4 == 0) :
        day_of_month[1] = 29
    else :
        day_of_month[1] = 28
    
    while True :
        new_day = current_day + 7
        new_month = current_month + new_day // (day_of_month[current_month-1] + 1)
        new_year = current_year + new_month // 13

        current_day = new_day % (day_of_month[current_month-1] + 1) + (new_day // (day_of_month[current_month-1] + 1))
        current_month = new_month % 13 + new_month // 13
        if new_year != current_year :
            current_year = new_year
            break
        
        if current_day == 13 :
            result += 1

print(result)