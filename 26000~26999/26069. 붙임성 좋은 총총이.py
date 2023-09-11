N = int(input())
rainbow_dance_group = ['ChongChong']

for i in range(N):
    person1, person2 = input().split()
    for j in range(len(rainbow_dance_group)):
        if person1 in rainbow_dance_group[j] and person2 != "ChongChong" and person2 not in rainbow_dance_group:
            rainbow_dance_group.append(person2)
        if person2 in rainbow_dance_group[j] and person1 != "ChongChong" and person1 not in rainbow_dance_group:
            rainbow_dance_group.append(person1)

print(len(rainbow_dance_group))
