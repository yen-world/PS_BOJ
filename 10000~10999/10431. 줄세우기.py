P = int(input())

for i in range(P) :
    test_case = list(map(int, input().split()))
    T, height = test_case[0], test_case[1:]
    line = []
    result = 0
    for j in range(len(height)) :
        line.append(height[j])
        for k in range(len(line)) :
            if line[k] > height[j] :
                line.insert(k ,line.pop())
                result += len(line[k+1:])
                break
    print(T, result)