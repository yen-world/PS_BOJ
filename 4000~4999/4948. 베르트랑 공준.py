def prime_number(start, end):
    sieve = [True] * end

    m = int(end ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, end, i):
                sieve[j] = False

    return [i for i in range(start, end) if (sieve[i] == True)]


number = 0

while True:
    number = int(input())
    if number == 0:
        break
    list = prime_number(number+1, number*2+1)
    print(len(list))
