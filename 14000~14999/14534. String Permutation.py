from itertools import permutations


T = int(input())

for i in range(T):
    string = input()
    print("Case # {}:".format(i + 1))
    for permutation in permutations(string):
        for char in permutation:
            print(char, end="")
        print()
