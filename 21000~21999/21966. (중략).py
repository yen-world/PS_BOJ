N = int(input())
S = input()

if len(S) <= 25:
    print(S)
else:
    front = S[:11]
    rear = S[-11:]
    center = S[11:-11]
    for i in range(len(center) - 1):
        if ord(center[i]) == 46:
            center = "......"
            front = S[:9]
            rear = S[-10:]
            print(front + center + rear)
            break
    else:
        center = "..."
        print(front + center + rear)
