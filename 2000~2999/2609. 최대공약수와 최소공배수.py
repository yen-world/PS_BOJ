def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    c = gcd(a, b)
    return int(a * b / c)


input_a, input_b = map(int, input().split())

print(gcd(input_a, input_b))
print(lcm(input_a, input_b))
