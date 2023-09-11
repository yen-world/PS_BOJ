case = int(input())

for i in range(case):
    west_site, east_site = map(int, input().split())
    n, m = 1, 1
    for j in range(east_site, east_site-west_site, -1):
        n *= j
    for j in range(1, west_site+1):
        m *= j
    print(n//m)
