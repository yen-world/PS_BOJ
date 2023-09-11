import sys
input = sys.stdin.readline

number, cnt = map(int, input().split())

num_list = list(map(int, input().split()))
s = [0 for i in range(len(num_list)+1)]

for i in range(len(num_list)):
    s[i+1] = s[i]+num_list[i]

for i in range(cnt):
    i, j = map(int, input().split())
    print(s[j]-s[i-1])
