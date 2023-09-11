asc = 65  # A의 아스키코드
dict = {}

for i in range(10, 36):
    dict[i] = asc
    asc += 1

N, B = map(int, input().split())
sqr = 0
temp = sqr
result = []
answer = ''

while True:
    if B ** sqr > N:
        sqr -= 1
        break
    else:
        sqr += 1

while N != 0:
    for i in range(1, B+1):
        if B ** sqr * i > N:
            result.append(i-1)
            N -= B ** sqr * (i-1)
            sqr -= 1
            break

while sqr > -1:
    sqr -= 1
    result.append(0)

for i in result:
    if 10 <= i <= 35:
        answer += chr(dict[i])
    else:
        answer += str(i)

print(answer)
