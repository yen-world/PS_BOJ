n = int(input())
dic = {'Y' : 0, 'M' : 0}
time = list(map(int, input().split()))

for i in time :
    y = (i // 30 + 1) * 10
    m = (i // 60 + 1) * 15
    dic['Y'] += y
    dic['M'] += m

if dic['Y'] > dic['M'] : print('M', dic['M'])
elif dic['Y'] < dic['M'] : print('Y', dic['Y'])
else : print('Y', 'M', dic['Y'])