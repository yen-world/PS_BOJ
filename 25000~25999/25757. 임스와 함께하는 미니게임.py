import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
person = set()

for i in range(N) :
    person.add(input())

if game == "Y" :
    print(len(person) // 1)
elif game == "F" :
    print(len(person) // 2)
else :
    print(len(person) // 3)