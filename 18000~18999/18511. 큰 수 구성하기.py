from itertools import product

N, K = map(int, input().split())
element = list(map(int, input().split()))
element.sort()
result = []

for i in range(1, 10):
    for j in product(element, repeat=i):
        value = ""
        for k in j:
            value += str(k)
        result.append(int(value))

for i in range(len(result)):
    if N < result[i]:
        print(result[i - 1])
        break
