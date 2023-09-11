op = input()  # 수식
num_list = []  # 문자열로 받은 수식을 분리하여 저장 할 리스트
index = 0  # 부호를 기준으로 나누기 위한 부호의 인덱스 변수
number = ''  # 숫자를 하나씩 받아서 저장하기 위한 변수

for i in range(len(op)):
    # 부호를 만나면 기존에 저장해둔 number를 리스트에 저장하고, 부호의 인덱스를 저장
    if op[i] == '-' or op[i] == '+':
        num_list.append(int(number))
        number = ''
        index = i
    # 숫자라면 number에 누적 시켜주고, 바로 앞의 부호가 -라면 -도 같이 저장함
    else:
        if op[index] == '-':
            number += '-'
            index = 0
        number += op[i]
num_list.append(int(number))

result = 0  # 결과값을 담을 변수
m_point = False  # 직전 값이 음수가 나왔음을 체크하기 위한 플래그 변수
for i in num_list:
    if i < 0:
        m_point = True
        result += i
    else:
        # 직전 값이 음수였다면 양수의 값을 음수로 변환하여 더함
        if m_point:
            result += -i
        # 음수가 나오지 않았다면 양수 값을 그대로 누적
        else:
            result += i
print(result)
