A, B = input().split()
reverse_A = ''
reverse_B = ''

for i in A:
    reverse_A = i + reverse_A

for i in B:
    reverse_B = i + reverse_B

print(max(int(reverse_A), int(reverse_B)))
