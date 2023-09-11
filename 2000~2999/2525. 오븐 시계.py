hour, minute = map(int, input().split())
time = int(input())

hour += int((minute + time) / 60)
minute = minute + time - 60
if (hour >= 24) :
    hour -= 24
        
print(hour, minute)