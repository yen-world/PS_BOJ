A, B = map(int, input().split())

print(A+B)

# A+B를 쓰지 않고 문자열로 계산
a, b = map(str, input().split())
temp = ''

if len(a) > len(b):
    for i in range(len(a)-len(b)):
        temp += '0'
    temp += b
    b = temp
else:
    for i in range(len(b)-len(a)):
        temp += '0'
    temp += a
    a = temp

result = [0 for i in range(len(a)+1)]
front = 0
end = 0

for i in range(len(a)-1, -1, -1):
    front = (int(a[i]) + int(b[i])) // 10
    end = (int(a[i]) + int(b[i])) % 10
    temp = result[i+1]
    result[i+1] = (end + result[i+1]) % 10
    result[i] = (front + ((end + temp) // 10))

while True:
    if result[0] == 0:
        result.pop(0)
    else:
        break

for i in result:
    print(i, end='')
