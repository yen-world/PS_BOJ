hour, minute = map(int, input().split())

if (minute >= 45) :
    minute -= 45
else :
    minute += 60
    minute -= 45
    if(hour != 0) :
        hour -= 1
    else :
        hour += 24
        hour -= 1
        
print(hour, minute)