count = 0
while True :
    o, w = map(int, input().split())
    flag = False
    if o == 0 and w == 0 :
        break
    count += 1

    while True :
        interaction, num = input().split()
        num = int(num)
        
        if not flag :
            if interaction == "E" :
                w -= num
            elif interaction == "F" :
                w += num

        if w <= 0 :
            flag = True

        if interaction == "#" :
            if flag :
                print(count, "RIP")
                break

            if o//2 < w < o*2 :
                print(count, ":-)")
            else :
                print(count, ":-(") 
            break      
                
