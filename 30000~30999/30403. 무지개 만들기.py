N = int(input())
string = input()
rainbow = []

for char in string:
    rainbow.append(char)

if (
    rainbow.count("r") >= 1
    and rainbow.count("o") >= 1
    and rainbow.count("y") >= 1
    and rainbow.count("g") >= 1
    and rainbow.count("b") >= 1
    and rainbow.count("i") >= 1
    and rainbow.count("v")
):
    if (
        rainbow.count("R") >= 1
        and rainbow.count("O") >= 1
        and rainbow.count("Y") >= 1
        and rainbow.count("G") >= 1
        and rainbow.count("B") >= 1
        and rainbow.count("I") >= 1
        and rainbow.count("V")
    ):
        print("YeS")
    else:
        print("yes")
elif (
    rainbow.count("R") >= 1
    and rainbow.count("O") >= 1
    and rainbow.count("Y") >= 1
    and rainbow.count("G") >= 1
    and rainbow.count("B") >= 1
    and rainbow.count("I") >= 1
    and rainbow.count("V")
):
    print("YES")
else:
    print("NO!")
