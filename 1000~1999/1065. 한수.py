def ArithmeticProgression(n):
    count = 0

    for i in range(1, n+1) :
        if (i >= 1000) : # 1000 이상의 경우
            num1 = int(i / 1000) # 천의 자리 숫자 추출
            num2 = int(i % 1000 / 100) # 백의 자리 숫자 추출
            num3 = int(i % 1000 % 100 / 10) # 십의 자리 숫자 추출
            num4 = int(i % 1000 % 100 % 10 / 1) # 일의 자리 숫자 추출
            sum = num1 + num2 + num3 + num4 # 자릿수의 합
            if(sum == (num1 + num4) * 4 / 2) : # 등차수열 공식
                count += 1 
        elif (i >= 100) : # 100 이상의 경우
            num2 = int(i % 1000 / 100) # 백의 자리 숫자 추출
            num3 = int(i % 1000 % 100 / 10) # 십의 자리 숫자 추출
            num4 = int(i % 1000 % 100 % 10 / 1) # 일의 자리 숫자 추출
            sum = num2 + num3 + num4 # 자릿수의 합
            if(sum == (num2 + num4) * 3 / 2) : # 등차수열 공식
                count += 1
        elif (i >= 10) :
                count += 1 
        elif (i >= 1) :
                count += 1
                
    return count
    
print(ArithmeticProgression(int(input())))