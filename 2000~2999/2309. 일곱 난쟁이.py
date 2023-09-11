key = []
for i in range(9):
    key.append(int(input()))
key.sort()

for i in range(9):
    for j in range(i+1, 9):
        if j < len(key):
            a = key[i]
            b = key[j]
            sum_value = sum(key) - a - b
            if (sum_value == 100):
                key.remove(a)
                key.remove(b)

for i in key:
    print(i)
