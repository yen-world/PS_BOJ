number = int(input())
facto = 1
count = 0

for i in range(1, number+1):
    facto *= i

facto = str(facto)

for i in reversed(facto):
    if i == '0':
        count += 1
    else:
        break

print(count)
