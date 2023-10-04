number = int(input())

if '7' not in str(number) and number % 7 != 0 :
    print(0)
elif '7' not in str(number) and number % 7 == 0 :
    print(1)
elif '7' in str(number) and number % 7 != 0 :
    print(2)
elif '7' in str(number) and number % 7 == 0 :
    print(3)
