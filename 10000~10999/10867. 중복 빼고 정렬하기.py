N = int(input())
numbers = list(set(list(map(int, input().split()))))
numbers.sort()
print(*numbers)
