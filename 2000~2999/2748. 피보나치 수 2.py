n = int(input())

fibonacci = [i for i in range(91)]
fibonacci[0] = 0
fibonacci[1] = 1

for i in range(2, 91) :
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

print(fibonacci[n])