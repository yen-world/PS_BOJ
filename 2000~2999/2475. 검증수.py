unique_number = list(map(int, input().split()))
veri_number = 0

for i in unique_number:
    veri_number += i**2

veri_number = veri_number % 10
print(veri_number)
