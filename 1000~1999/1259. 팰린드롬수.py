while True:
    number = int(input())
    number = str(number)
    if number == "0":
        break
    else:
        flag = True
        for i in range(len(number)//2):
            if number[i] != number[-i-1]:
                flag = False
                break
        if flag:
            print("yes")
        else:
            print("no")
