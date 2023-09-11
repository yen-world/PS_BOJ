s1, s2, s3 = map(int, input().split())
dice_dict = {}
result = 0
max_value = 0

for i in range(3, s1 + s2 + s3 + 1):
    dice_dict[i] = 0

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            dice_dict[i + j + k] += 1

for i in dice_dict.keys():
    if max_value < dice_dict[i]:
        max_value = dice_dict[i]
        result = i

print(result)
