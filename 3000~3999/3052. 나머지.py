list = []
rest = []
count = 0

for i in range(10) :
    list.append(int(input()))
    list[i] = list[i] % 42
    
for data in list :
    if data not in rest :
        rest.append(data)
        count += 1    

print(count)