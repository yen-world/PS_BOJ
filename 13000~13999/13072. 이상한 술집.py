def binary_search():
    low, high, mid = 1, max_teapot, max_teapot
    result = 0
    global k
    
    while low <= high:
        m = 0
        mid = (low + high) // 2
        for i in range(n) :
            m += teapot[i] // mid
        if m >= k :
            low = mid + 1
            result = mid
        else :
            high = mid - 1
            
    return result

n, k = map(int, input().split())
teapot = [int(input()) for i in range(n)]
max_teapot = max(teapot)

print(binary_search())