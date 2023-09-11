import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    note1 = int(input())
    note1_list = list(map(int, input().split()))
    dic = {}
    for j in range(note1):
        dic[note1_list[j]] = 1

    note2 = int(input())
    note2_list = list(map(int, input().split()))
    for j in range(note2):
        if note2_list[j] in dic.keys():
            print(1)
        else:
            print(0)
