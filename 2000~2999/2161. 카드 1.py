N = int(input())
card = [i for i in range(1, N+1)]

while len(card) > 1 :
    print(card.pop(0), end=' ')
    card.append(card.pop(0))
print(*card)