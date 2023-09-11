N = int(input())
count = 0

list = list(map(int, input().split()))

number = int(input())

for i in range(N) :
    if list[i] == number :
        count += 1
        
print(count)
print(list.count(number))