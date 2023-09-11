import sys
input = sys.stdin.readline

case = int(input())
prime = []
num_list = [True] * 1000001

for i in range(2, 1000001):
    if num_list[i] == True:
        prime.append(i)
        for j in range(i+i, 1000001, i):
            num_list[j] = False

for i in range(case):
    number = int(input())
    count = 0
    for j in prime:
        if j > number:
            break
        if num_list[number-j] and j <= number-j:
            count += 1
    print(count)
