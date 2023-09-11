access_count = int(input())
staff = {}

for i in range(access_count):
    name, record = input().split()
    staff[name] = record
sorted_list = sorted(staff, reverse=True)

for i in sorted_list:
    if staff[i] == "enter":
        print(i)
