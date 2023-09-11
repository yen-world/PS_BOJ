import sys
input = sys.stdin.readline

N, M = map(int, input().split())

picture_book_name = {}
picture_book_number = {}
result = []
for i in range(1, N+1):
    picture_book_name[i] = input().rstrip()
    picture_book_number[picture_book_name[i]] = i

for i in range(M):
    command = input().rstrip()
    if ord(command[0]) >= 49 and ord(command[0]) <= 57:
        command = int(command)
        result.append(picture_book_name[command])
    else:
        result.append(picture_book_number[command])

for i in result:
    print(i)
