import sys

N = int(input())
A = []
number = ""

for char in sys.stdin.read():
    if char.isdigit():
        number += char
    else:
        A.append(int(number))
        number = ""

A.sort()

result = 0

for i in range(int(N)):
    if int(A[i]) == result:
        print(result)
        break

    result = int(A[i])
