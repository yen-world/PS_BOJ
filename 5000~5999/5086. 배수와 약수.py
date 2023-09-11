while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if b % a == 0:
        print("factor")
    if a % b == 0:
        print("multiple")
    if b % a != 0 and a % b != 0:
        print("neither")
