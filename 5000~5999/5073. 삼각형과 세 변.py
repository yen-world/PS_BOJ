while True:
    A, B, C = map(int, input().split())
    max_value = max(A, B, C)
    sum_value = A+B+C

    if A == 0 and B == 0 and C == 0:
        break

    if A == B == C:
        print("Equilateral")
    elif A == B or A == C or B == C:
        if sum_value - max_value > max_value:
            print("Isosceles")
        else:
            print("Invalid")
    elif A != B != C:
        if sum_value - max_value > max_value:
            print("Scalene")
        else:
            print("Invalid")
