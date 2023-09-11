list = []
max = 0
index = 0

for i in range(9) :
    list.append(int(input()))
    
for i in range(len(list)) :
    if (list[i] > max) :
        max = list[i]
        index = i
        
print(max)
print(index+1)