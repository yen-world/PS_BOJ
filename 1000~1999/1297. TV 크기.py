d, h, w = map(int, input().split())

h_square = h**2
w_square = w**2
length = (h_square + w_square) ** 0.5
ratio = d / length

print(int(h * ratio), int(w * ratio))
