n = int(input())
total_mass = 0
total_value = 0

for i in range(n):
    t, w, h, l = input().split()
    w = int(w)
    h = int(h)
    l = int(l)

    if t == "A":
        weight_a = w // 12
        height_a = h // 12
        length_a = l // 12
        apple = weight_a * height_a * length_a
        total_value += 4000 * apple
        box = 1000 + 500 * apple
    else:
        box = 6000

    total_mass += box

print(total_mass)
print(total_value)
