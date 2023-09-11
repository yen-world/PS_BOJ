x, y, w, h = map(int, input().split())
median_w = w/2
median_h = h/2
if (x < median_w):
    if (y < median_h):
        print(min(x, y))
    else:
        if (x < h-y):
            print(x)
        else:
            print(h-y)
else:
    if (y <= median_h):
        if (w-x < y):
            print(w-x)
        else:
            print(y)
    else:
        print(min(w-x, h-y))
