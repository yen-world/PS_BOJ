import sys
input = sys.stdin.readline

numbers = list(map(str, input().split()))
count = 0
result = []

for i in range(1, len(numbers)) :
    result.append(int("".join(reversed(numbers[i].rstrip("0")))))
    count += 1

while count < int(numbers[0]) :
    temp = list(map(str, input().split()))

    for i in range(len(temp)) :
        reverse_number = "".join(reversed(temp[i].rstrip("0")))
        result.append(int(reverse_number))
        count += 1

result.sort()

print(*result, sep='\n')