import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

dict = {}

for i in N_list:
    dict[i] = 0

for i in N_list:
    dict[i] += 1

for i in M_list:
    if i in dict:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')
