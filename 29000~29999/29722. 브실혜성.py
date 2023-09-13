year, month, day = map(int, input().split("-"))
n = int(input())

day += n

while day > 30:
    day -= 30
    month += 1

while month > 12:
    month -= 12
    year += 1

if day < 10:
    day = "0" + str(day)

if month < 10:
    month = "0" + str(month)

print("{}-{}-{}".format(year, month, day))
