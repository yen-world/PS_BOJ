N, K = map(int, input().split())
cnt = 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        if K == cnt:
            print(i)
            break

if K > cnt:
    print(0)
