def get_gcd(n, m):
    if m == 0:
        return n
    else:
        return get_gcd(m, n % m)


ring = int(input())
radius_list = list(map(int, input().split()))

for i in range(1, len(radius_list)):
    gcd = get_gcd(radius_list[0], radius_list[i])
    print("{}/{}".format(radius_list[0]//gcd, radius_list[i]//gcd))
