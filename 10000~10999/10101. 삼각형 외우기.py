A = int(input())
B = int(input())
C = int(input())
result = A+B+C

if A == 60 and B == 60 and C == 60:
    print("Equilateral")
elif result == 180:
    if A == B or A == C or B == C:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
