def d(n) :
    list = []
    
    list.append(int(n / 10000))
    num1 = n % 10000
    
    list.append(int(num1 / 1000))
    num2 = num1 % 1000
    
    list.append(int(num2 / 100))
    num3 = num2 % 100
    
    list.append(int(num3 / 10))
    num4 = num3 % 10
    
    list.append(int(num4 / 1))
    
    return n + sum(list)

number = [i for i in range(1, 10001)]

for i in range(1, 10001):
    if ( d(i) in number) :
        number.remove(d(i))
        
for i in number :
    print(i)