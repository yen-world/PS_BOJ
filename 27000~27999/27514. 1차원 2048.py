import sys
input = sys.stdin.readline

n = int(input())
list_2048 = list(map(int, input().split()))
dic = dict()

for i in range(0, 63):
    dic[2**i] = 0

for i in range(n):
    if list_2048[i] != 0:
        dic[list_2048[i]] += 1

for key in dic.keys():
    if dic[key] >= 2:
        dic[key*2] += dic[key]//2
        dic[key] = dic[key] % 2

for key in dic.keys():
    if dic[key] != 0:
        max_value = key

print(max_value)
