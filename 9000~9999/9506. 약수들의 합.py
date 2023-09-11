while True:
    n = int(input())
    sum_list = []
    if n == -1:
        break
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            sum_list.append(i)
            sum_list.append(n//i)
    sum_list.sort()
    sum_list.pop()
    if n == sum(sum_list):
        print(n, '=', end=' ')
        for i in range(len(sum_list)-1):
            print(sum_list[i], '+', end=' ')
        print(sum_list[-1])
    else:
        print(n, 'is NOT perfect.')
