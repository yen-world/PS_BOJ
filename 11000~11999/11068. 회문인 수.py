T = int(input())

for i in range(T):
    num = int(input())
    isPalindrome = False
    for radix in range(2, 65):
        n = num
        radix_n_num = []

        while n > 0:
            n, mod = divmod(n, radix)
            radix_n_num.append(mod)
        radix_n_num = radix_n_num[::-1]

        for j in range(len(radix_n_num) // 2):
            if radix_n_num[j] != radix_n_num[-j - 1]:
                break
        else:
            isPalindrome = True

        if isPalindrome:
            print(1)
            break
    else:
        print(0)
