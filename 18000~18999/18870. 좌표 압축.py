import sys
input = sys.stdin.readline

N = int(input())
num_list = []
temp_list = []

num_list = list(map(int, input().split()))
temp_list = list(set(num_list))
temp_list.sort()
result = {}

for i in range(len(temp_list)):
    result[temp_list[i]] = i

for i in range(len(num_list)):
    print(result[num_list[i]], end=' ')
