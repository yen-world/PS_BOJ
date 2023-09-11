def merge_sort(data, left, right, value):
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid, value)
        merge_sort(data, mid+1, right, value)
        merge(data, left, right, mid, value)


def merge(data, left, right, mid, value):
    global count
    global checker
    i = left
    j = mid + 1
    t = 0
    while (i <= mid and j <= right):
        if (data[i] <= data[j]):
            temp[t] = data[i]
            t += 1
            i += 1
        else:
            temp[t] = data[j]
            t += 1
            j += 1
    while (i <= mid):
        temp[t] = data[i]
        t += 1
        i += 1
    while (j <= right):
        temp[t] = data[j]
        t += 1
        j += 1
    i = left
    t = 0
    while (i <= right):
        count += 1
        if count == value:
            print(temp[t])
            checker = True
            break
        data[i] = temp[t]
        i += 1
        t += 1


A, K = map(int, input().split())
data = list(map(int, input().split()))
temp = [0 for i in range(len(data))]
count = 0
checker = False
merge_sort(data, 0, A-1, K)
if not checker:
    print(-1)
