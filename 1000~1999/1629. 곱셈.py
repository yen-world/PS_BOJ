def power(C, n, m) :
    if n == 1 :
        return C % m
    else :
        x = power(C, n//2, m)
        if n % 2 == 0 :
            return x * x % m
        else :
            return C * x * x % m

a, b, c = (map(int, input().split()))

print(power(a,b,c))