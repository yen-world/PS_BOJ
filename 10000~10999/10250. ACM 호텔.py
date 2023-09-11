import math

test_num = int(input())

for i in range(test_num):
    height, room, guest = map(int, input().split())
    room_number = int(math.ceil(guest / height))
    if guest % height != 0:
        floor_numer = int(guest % height)
    else:
        floor_numer = int(guest / (guest / height))

    if (room_number / 10 < 1):
        print(floor_numer, "0", room_number, sep="")
    else:
        print(floor_numer, room_number, sep="")
