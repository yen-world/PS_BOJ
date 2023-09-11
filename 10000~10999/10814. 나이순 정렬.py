N = int(input())
member = []
new_list = []

for i in range(N):
    member.append(input().split())
    member[i][0] = int(member[i][0])

member.sort(key=lambda x: x[0])

for i in range(len(member)):
    print("{} {}".format(member[i][0], member[i][1]))
