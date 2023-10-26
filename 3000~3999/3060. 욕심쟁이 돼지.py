T = int(input())

for i in range(T) :
    N = int(input())
    first_meal = list(map(int, input().split()))
    result = 1
    temp = first_meal

    if sum(first_meal) > N :
        print(result)
        continue
    
    while True :
        tomorrow_meal = []
        result += 1
        for j in range(6) :
            tomorrow_meal.append(temp[j] + temp[(j - 1) % 6] + temp[(j + 1) % 6] + temp[(j + 3) % 6])
        temp.clear()
        temp.extend(tomorrow_meal)
        
        if sum(tomorrow_meal) > N :
            break

    print(result)
