def lowerBound():
    low = 1
    high = 1000000000

    while low < high:
        mid = (low + high) // 2
        temp_x = x + mid
        temp_y = y + mid
        temp_z = temp_y * 100 / temp_x

        if z + 1 <= temp_z:
            high = mid
        else:
            low = mid + 1
    return low


x, y = map(int, input().split())
z = (y * 100) / x
z = int(z)

if z >= 99:
    print(-1)
else:
    print(lowerBound())
