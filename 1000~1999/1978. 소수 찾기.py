N = int(input())
list = list(map(int, input().split()))
count = 0

for i in range(len(list)) :
    for j in range(2, list[i]+1) :
        if list[i] % j == 0 :
            if j == list[i] :
                count += 1
            else :
                break
            
print(count)