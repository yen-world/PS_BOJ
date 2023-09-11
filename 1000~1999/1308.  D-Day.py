import datetime

current_date = list(map(int, input().split()))
current_date = datetime.date(current_date[0], current_date[1], current_date[2])

d_day_date = list(map(int, input().split()))
d_day_date = datetime.date(d_day_date[0], d_day_date[1], d_day_date[2])

if current_date.year + 1000 < d_day_date.year:
    print("gg")
    exit()
elif current_date.year + 1000 == d_day_date.year:
    if current_date.month <= d_day_date.month and current_date.day <= d_day_date.day:
        print("gg")
        exit()

result = (d_day_date - current_date).days
print("D-{}".format(result))
