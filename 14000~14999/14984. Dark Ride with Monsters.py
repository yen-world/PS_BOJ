def list_sort():
    count = 0
    i = 0
    while i < n-1:
        if num_list[i] != i+1:
            idx = num_list[i]
            num_list[i], num_list[idx-1] = num_list[idx-1], num_list[i]
            count += 1
        else:
            i += 1
    return count


while True:
    try:
        n = int(input())
    except EOFError:
        break
    num_list = list(map(int, input().split()))
    print(list_sort())
