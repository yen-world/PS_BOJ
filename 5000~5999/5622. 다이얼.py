word = input().upper()
count = 2
time = 0

for i in word:
    num = ord(i)-65
    if (0 <= num <= 2):
        count += 1
        time += count
    elif (3 <= num <= 5):
        count += 2
        time += count
    elif (6 <= num <= 8):
        count += 3
        time += count
    elif (9 <= num <= 11):
        count += 4
        time += count
    elif (12 <= num <= 14):
        count += 5
        time += count
    elif (15 <= num <= 18):
        count += 6
        time += count
    elif (19 <= num <= 21):
        count += 7
        time += count
    elif (22 <= num <= 25):
        count += 8
        time += count
    count = 2

print(time)
