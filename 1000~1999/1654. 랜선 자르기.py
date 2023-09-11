import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan_cable = []

for i in range(K):
    lan_cable.append(int(input()))

max_length = max(lan_cable)

start = 0
end = max_length
mid = max_length // 2

first_length_sum = 0
second_length_sum = 0

while True:
    first_length_sum = 0
    second_length_sum = 0
    for i in range(len(lan_cable)):
        if mid == 0:
            first_length_sum += lan_cable[i] // 1
            second_length_sum += lan_cable[i] // 1
        else:
            first_length_sum += lan_cable[i] // mid
            second_length_sum += lan_cable[i] // (mid+1)
    if start <= end:
        if N == first_length_sum and N > second_length_sum:
            break
        elif N == first_length_sum:
            start = mid + 1
            mid = (start + end) // 2
        elif N > first_length_sum:  # 자른 값이 크면? 줄여야함
            end = mid - 1
            mid = (start + end) // 2
        elif N < first_length_sum:  # 자른 값이 작으면? 늘려야함
            start = mid + 1
            mid = (start + end) // 2
    else:
        break

print(mid)
