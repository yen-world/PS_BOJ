import sys
input = sys.stdin.readline

count = int(input())
meeting = []
result = []

for i in range(count):
    meeting.append(list(map(int, input().split())))
meeting.sort()
meeting.append([1e6, 1e6])

temp = []
temp.append(meeting[0])
for i in range(count):
    if temp[0][0] == temp[0][1]:
        result.append(temp[0])
        temp.pop()
        temp.append(meeting[i+1])
    else:
        if temp[0][1] <= meeting[i+1][0]:
            result.append(temp[0])
            temp.pop()
            temp.append(meeting[i+1])
        else:
            if temp[0][1] >= meeting[i+1][1]:
                temp.pop()
                temp.append(meeting[i+1])

print(len(result))
