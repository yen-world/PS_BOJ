n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
min_price = 1e9

for i in range(n-1) :
    if min_price > price[i] :
        min_price = price[i]
    result += min_price * distance[i]
    
print(result)