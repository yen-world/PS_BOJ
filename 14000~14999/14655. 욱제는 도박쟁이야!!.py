N = int(input())
coin1 = list(map(int, input().split()))
coin2 = list(map(int, input().split()))

for i in range(len(coin1)):
    if coin1[i] < 0:
        coin1[i] = -coin1[i]


for i in range(len(coin2)):
    if coin2[i] > 0:
        coin2[i] = -coin2[i]

result = sum(coin1) - sum(coin2)

print(result)
