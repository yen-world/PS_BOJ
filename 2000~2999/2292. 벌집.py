N = int(input())
count = 1

if N == 1:
    print(1)
    exit()

N = N-1

while True:
    if N-6*count >= 1:
        N = N-6*count
        count += 1
    else:
        count += 1
        break

print(count)
