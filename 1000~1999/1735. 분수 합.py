def get_gcd(A, B):
    if A % B == 0:
        return B
    else:
        return get_gcd(B, A % B)


A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
gcd = get_gcd(B1, B2)
lcm = B1 * B2 // gcd

numeraotr = A1 * lcm//B1 + A2 * lcm//B2
denominator = B1 * B2 // gcd
gcd = get_gcd(numeraotr, denominator)
print(numeraotr//gcd, denominator//gcd)
