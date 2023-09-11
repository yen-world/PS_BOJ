max_height = 0
max_width = 0

melon = int(input())
ground = [list(map(int, input().split())) for i in range(6)]

for i in range(6):
    if ground[i][0] == 1 or ground[i][0] == 2:
        if max_width < ground[i][1]:
            max_width = ground[i][1]
            width_index = i
    if ground[i][0] == 3 or ground[i][0] == 4:
        if max_height < ground[i][1]:
            max_height = ground[i][1]
            height_index = i
if abs(width_index-height_index) > 1:
    index = min(width_index, height_index)
else:
    index = max(width_index, height_index)

big_ground = max_width * max_height
small_ground = ground[(index + 2) % 6][1] * ground[(index + 3) % 6][1]
result_ground = (big_ground-small_ground) * melon
print(result_ground)
