N = int(input())
fibonacci = [0] * 82
fibonacci[1] = 1
fibonacci[2] = 1
result = [0] * 81

for i in range(3, 82):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

for i in range(1, 81):
    result[i] = (fibonacci[i + 1] + fibonacci[i]) * 2

print(result[N])
