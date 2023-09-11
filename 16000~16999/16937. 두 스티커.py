h, w = map(int, input().split())
n = int(input())
sticky = []
max_value = 0

for i in range(n):
    sticky.append(list(map(int, input().split())))

for i in range(n):
    fir_h, fir_w = sticky[i]
    for j in range(i+1, n):
        sec_h, sec_w = sticky[j]
        if (fir_h + sec_h <= h and max(fir_w, sec_w) <= w) or (max(fir_h, sec_h) <= h and fir_w + sec_w <= w):
            max_value = max(max_value, fir_h * fir_w + sec_h * sec_w)
        elif (fir_w + sec_h <= h and max(fir_h, sec_w) <= w) or (max(fir_w, sec_h) <= h and fir_h + sec_w <= w):
            max_value = max(max_value, fir_h * fir_w + sec_h * sec_w)
        elif (fir_h + sec_w <= h and max(fir_w, sec_h) <= w) or (max(fir_h, sec_w) <= h and fir_w + sec_h <= w):
            max_value = max(max_value, fir_h * fir_w + sec_h * sec_w)
        elif (fir_w + sec_w <= h and max(fir_h, sec_h) <= w) or (max(fir_w, sec_w) <= h and fir_h + sec_h <= w):
            max_value = max(max_value, fir_h * fir_w + sec_h * sec_w)

print(max_value)
