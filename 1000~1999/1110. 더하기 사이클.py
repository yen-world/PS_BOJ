N = int(input())
count = 1
temp = N
while True :
    front = int(temp / 10)
    reer = int(temp % 10)
    sum = front + reer
    
    if (reer * 10 + sum % 10 != N) :
        temp = reer * 10 + sum % 10
        count += 1
    else :
        print(count)
        break