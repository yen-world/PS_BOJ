def Get_gcd(a, b) :
    if (b == 0) :
        return a
    else :
        return Get_gcd(b, a%b)    



n, m = map(int, input().split(':'))
gcd = Get_gcd(n, m)
print("{}:{}".format(n//gcd, m//gcd))