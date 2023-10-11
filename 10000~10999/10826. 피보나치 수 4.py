n = int(input())

fibonacci = [0] * 10001
fibonacci[0] = 0
fibonacci[1] = 1

for i in range(2, 10001) :
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

print(fibonacci[n])