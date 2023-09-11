first_color = input()
second_color = input()
third_color = input()

result = ''

if first_color == "black":
    result += '0'
elif first_color == "brown":
    result += '1'
elif first_color == "red":
    result += '2'
elif first_color == "orange":
    result += '3'
elif first_color == "yellow":
    result += '4'
elif first_color == "green":
    result += '5'
elif first_color == "blue":
    result += '6'
elif first_color == "violet":
    result += '7'
elif first_color == "grey":
    result += '8'
elif first_color == "white":
    result += '9'

if second_color == "black":
    result += '0'
elif second_color == "brown":
    result += '1'
elif second_color == "red":
    result += '2'
elif second_color == "orange":
    result += '3'
elif second_color == "yellow":
    result += '4'
elif second_color == "green":
    result += '5'
elif second_color == "blue":
    result += '6'
elif second_color == "violet":
    result += '7'
elif second_color == "grey":
    result += '8'
elif second_color == "white":
    result += '9'

result = int(result)
if third_color == "black":
    result *= 1
elif third_color == "brown":
    result *= 10
elif third_color == "red":
    result *= 100
elif third_color == "orange":
    result *= 1000
elif third_color == "yellow":
    result *= 10000
elif third_color == "green":
    result *= 100000
elif third_color == "blue":
    result *= 1000000
elif third_color == "violet":
    result *= 10000000
elif third_color == "grey":
    result *= 100000000
elif third_color == "white":
    result *= 1000000000

print(result)
