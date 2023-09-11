n = input()
n_list = [int(i) for i in n]
result = "NO"

for i in range(1, len(n)):
    first_list = n_list[:i]
    second_list = n_list[i:]
    first_value = 1
    second_value = 1
    for j in first_list:
        first_value *= j

    for j in second_list:
        second_value *= j

    if first_value == second_value:
        result = "YES"
        break

print(result)
