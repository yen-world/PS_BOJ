N, M = map(int, input().split())
J = int(input())
pos = []
result = 0

for i in range(J) :
    pos.append(int(input()))

left_index, right_index = 1, M

for i in range(J) :
    if left_index <= pos[i] <= right_index :
        continue
    if left_index > pos[i] : # 현재 바구니보다 왼쪽에 떨어질경우
        result += left_index - pos[i]
        left_index -= left_index - pos[i]
        right_index = left_index + M - 1
    elif right_index < pos[i] : # 현재 바구니보다 오른쪽에 떨어질경우
        result += pos[i] - right_index
        right_index += pos[i] - right_index
        left_index = right_index - M + 1

print(result)