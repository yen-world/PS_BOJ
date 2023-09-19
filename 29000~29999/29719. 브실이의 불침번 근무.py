def power(a, b) :
    if b == 0 :
        return 1
    
    value = power(a, b//2)

    if b % 2 == 0 :
        return value * value
    else :
        return a * value * value


n, m = map(int, input().split())
print((power(m, n) - power(m-1, n)) % 1000000007)
