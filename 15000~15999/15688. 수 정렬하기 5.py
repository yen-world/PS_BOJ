import sys
input = sys.stdin.readline

N = int(input())
numbers = []

for i in range(N) :
    numbers.append(int(input()))

numbers.sort()

for number in numbers :
    print(number)