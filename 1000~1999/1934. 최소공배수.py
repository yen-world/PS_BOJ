def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


case = int(input())

for i in range(case):
    num1, num2 = map(int, input().split())
    print(num1 * num2 // gcd(num1, num2))
