n = int(input())
main_stack = list(map(int, input().split()))
main_stack = list(reversed(main_stack))
sub_stack = []
count = 1

while True :
    if count == n :
        print("Nice")
        break

    if main_stack and main_stack[-1] == count :
        main_stack.pop()
        count += 1
        continue
    elif sub_stack and sub_stack[-1] == count :
        sub_stack.pop()
        count += 1
        continue

    else :
        if main_stack :
            sub_stack.append(main_stack.pop())
        else :
            print("Sad")
            break

    