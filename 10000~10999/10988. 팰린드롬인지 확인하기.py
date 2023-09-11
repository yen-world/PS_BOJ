string = input()

for i in range(len(string)//2):
    if string[i] != string[-i-1]:
        print(0)
        exit()
print(1)
