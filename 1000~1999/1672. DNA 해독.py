import sys

input = sys.stdin.readline

dna_matrix = [
    ["A", "C", "A", "G"],
    ["C", "G", "T", "A"],
    ["A", "T", "C", "G"],
    ["G", "A", "G", "T"],
]

n = int(input())
dna = input().rstrip()

if len(dna) <= 1:
    print(dna)
else:
    result = dna[-1]
    for i in range(1, n):
        a = result
        b = dna[-i - 1]
        if a == "A":
            a = 0
        elif a == "G":
            a = 1
        elif a == "C":
            a = 2
        else:
            a = 3

        if b == "A":
            b = 0
        elif b == "G":
            b = 1
        elif b == "C":
            b = 2
        else:
            b = 3

        result = dna_matrix[b][a]
    print(result)
