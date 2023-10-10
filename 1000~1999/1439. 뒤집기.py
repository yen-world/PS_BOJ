S = input()
zero, one = 0, 0
temp = -1

for i in S:
    if i != temp:
        temp = i
        if temp == "0":
            zero += 1
        else:
            one += 1

print(min(zero, one))
