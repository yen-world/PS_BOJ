def fibonacci(n):
    if mem[n] == None:
        mem[n] = fibonacci(n-1) + fibonacci(n-2)
        return mem[n]
    else:
        return mem[n]


case = int(input())

mem = [None for i in range(41)]
mem[0] = 0
mem[1] = 1

for i in range(case):
    n = int(input())
    fibonacci(n)
    count0 = mem[n-1]
    count1 = mem[n]
    if n == 0:
        count0 = 1
    print(count0, count1)
