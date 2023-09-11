input_num = int(input())

line = 1
line_check = 1

while True:
    if input_num > line_check:
        line += 1
        line_check += line
    else:
        break

if line % 2 == 1:
    denominator = line_check - input_num + 1
    numerator = input_num - line_check + line
else:
    denominator = input_num - line_check + line
    numerator = line_check - input_num + 1

print(denominator, "/", numerator, sep="")
