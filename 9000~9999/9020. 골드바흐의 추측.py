import sys


def prime_number(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if (sieve[i] == True)]


case = int(input())
prime_list = prime_number(10000)

for i in range(case):
    check_number = int(sys.stdin.readline())
    for i in range(check_number//2, 1, -1):
        if i in prime_list and check_number-i in prime_list:
            num1 = i
            num2 = check_number-i
            break
    print(min(num1, num2), max(num1, num2))
