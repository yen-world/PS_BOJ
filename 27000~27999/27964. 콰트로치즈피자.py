n = int(input())
toppings = list(set(list(input().split())))
dic = dict()
count = 0

for i in range(len(toppings)):
    if toppings[i].endswith("Cheese"):
        if toppings[i].upper() not in dic:
            dic[toppings[i].upper()] = 1

if len(dic) >= 4:
    print("yummy")
else:
    print("sad")
