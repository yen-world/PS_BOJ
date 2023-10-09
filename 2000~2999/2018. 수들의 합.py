N = int(input())
start = 0
end = 0
value = 0
result = 0

while end <= N:
    if value < N:
        end += 1
        value += end
    elif value > N:
        start += 1
        value -= start
    else:
        result += 1
        end += 1
        value += end

print(result)
