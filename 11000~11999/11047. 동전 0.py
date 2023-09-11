coin, value = map(int, input().split())
kind = []
max_value = 0
count = 0

for i in range(coin):
    kind.append(int(input()))

kind.reverse()

for i in range(len(kind)):
    if value // kind[i] >= 1:
        max_value = kind[i]
        index = i
        break

while value != 0 and max_value > 0:
    count += value // max_value
    value = value % max_value
    if index+1 < len(kind):
        index += 1
        max_value = kind[index]

print(count)
