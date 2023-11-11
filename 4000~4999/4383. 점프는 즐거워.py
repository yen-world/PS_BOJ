while True:
    try:
        numbers = list(map(int, input().split()))
        n = numbers[0]
    except EOFError:
        break

    if n == 1:
        print("Jolly")
    else:
        new_numbers = []
        count = 1

        for i in range(1, n):
            new_numbers.append(abs(numbers[i] - numbers[i + 1]))

        new_numbers.sort()
        for i in new_numbers:
            if i == count:
                count += 1
            else:
                print("Not jolly")
                break
        else:
            print("Jolly")
