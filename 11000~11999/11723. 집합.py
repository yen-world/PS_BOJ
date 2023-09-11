import sys
input = sys.stdin.readline

operation = int(input())
S = []

for i in range(operation):
    command = input()
    if 'add' in command:
        command, number = command.split()
        number = int(number)
        if number not in S:
            S.append(number)
    elif 'remove' in command:
        command, number = command.split()
        number = int(number)
        if number in S:
            S.remove(number)
    elif 'check' in command:
        command, number = command.split()
        number = int(number)
        if number in S:
            print(1)
        else:
            print(0)
    elif 'toggle' in command:
        command, number = command.split()
        number = int(number)
        if number in S:
            S.remove(number)
        else:
            S.append(number)
    elif 'all' in command:
        S = [i for i in range(1, 21)]
    elif 'empty' in command:
        S.clear()
