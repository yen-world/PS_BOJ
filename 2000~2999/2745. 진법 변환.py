asc = 65  # A의 아스키코드
dict = {}

for i in range(10, 36):
    dict[asc] = i
    asc += 1

N, B = input().split()
B = int(B)
length = len(N) - 1
result = 0

for i in range(len(N)):
    if 65 <= ord(N[i]) <= 90:
        result += B ** length * dict[ord(N[i])]
        length -= 1
    else:
        result += B ** length * int(N[i])
        length -= 1
print(result)
