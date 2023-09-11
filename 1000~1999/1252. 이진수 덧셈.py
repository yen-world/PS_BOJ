binary_a, binary_b = input().split()
decimal_a, decimal_b = 0, 0

radix = 1
for i in reversed(binary_a):
    if i == "1":
        decimal_a += radix
    radix *= 2

radix = 1
for i in reversed(binary_b):
    if i == "1":
        decimal_b += radix
    radix *= 2

print(bin(decimal_a + decimal_b)[2:])
