def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

# num_list: 입력 리스트, new_list: 값을 뺀 리스트, gcd_list: 최대공약수의 약수 리스트
number = int(input())
num_list = []
new_list = []
gcd_list = []

# 숫자 리스트 입력 받고 정렬
for i in range(number):
    num_list.append(int(input()))
num_list.sort()

# num_list[i]와 num_list[i-1]의 값을 new_list에 넣고 정렬
for i in range(len(num_list)-1, 0, -1):
    new_list.append(num_list[i]-num_list[i-1])
new_list.sort()

# 23~33 모든 수의 최대공약수를 구하고, 최대공약수의 약수를 gcd_list에 넣음
gcd = new_list[0]

for i in range(1, len(new_list)):
    gcd = get_gcd(gcd, new_list[i])

for i in range(2, int(gcd ** (1/2) + 1)):
    if gcd % i == 0:
        gcd_list.append(i)
        gcd_list.append(gcd//i)
gcd_list.append(gcd)

# 중복 제거 이후, list로 변환 및 정렬하여 전개 연산자로 출력
gcd_list = set(gcd_list)
result = list(gcd_list)
result.sort()

print(*result)
