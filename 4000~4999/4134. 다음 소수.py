case = int(input())

for i in range(case):
    num = int(input())
    while True:
        for j in range(2, int(num**(1/2))+1):
            if num % j == 0:
                num += 1
                break
        else:
            if num < 2:
                print(2)
                break
            else:
                print(num)
                break
