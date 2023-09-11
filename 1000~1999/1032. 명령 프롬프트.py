n = int(input())
command = []

for i in range(n):
    command.append(list(input()))

command_length = len(command[0])
for i in range(command_length):
    for j in range(n):
        if command[0][i] != command[j][i]:
            command[0][i] = '?'
            break

for i in command[0]:
    print(i, end='')
