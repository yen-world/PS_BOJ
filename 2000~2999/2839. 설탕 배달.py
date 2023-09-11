kg = int(input())
count = 0
while kg != 0:
    if kg % 5 == 0:
        kg -= 5
        count += 1
    elif kg % 3 == 0:
        kg -= 3
        count += 1
    elif kg > 5:
        kg -= 5
        count += 1
    else:
        count = -1
        break

print(count)
