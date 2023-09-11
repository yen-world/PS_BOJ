import sys
input = sys.stdin.readline

case = int(input())
word_list = []

for i in range(case):
    word_list.append(input().rstrip())

word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x), x))

for i in word_list:
    print(i)
