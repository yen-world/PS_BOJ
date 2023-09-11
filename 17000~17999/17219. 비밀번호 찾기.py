case, search = map(int, input().split())
info = {}

for i in range(case):
    site, password = map(str, input().split())
    info[site] = password

for i in range(search):
    print(info[input()])
