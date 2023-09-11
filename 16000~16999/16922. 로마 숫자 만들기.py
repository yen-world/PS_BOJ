from itertools import combinations_with_replacement

n = int(input())
result = []

for combi in combinations_with_replacement([1, 5, 10, 50], n):
    result.append(sum(combi))
print(len(set(result)))
