import sys
input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]
result = 0

while True :
    for i in range(1, N) :
        if li[0] <= li[i] :
            break
    else :
        break
    
    max_value = 0

    for i in range(1, N) :
        if max_value <= li[i] :
            max_value = li[i]
            max_index = i

    li[max_index] -= 1
    li[0] += 1
    result += 1

print(result)