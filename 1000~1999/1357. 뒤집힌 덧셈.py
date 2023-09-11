def rev(num):
    value = ""
    for i in reversed(num):
        value += i
    value = int(value)
    return value


x, y = input().split()
x = rev(x)
y = rev(y)
result = rev(str(x + y))
print(result)
