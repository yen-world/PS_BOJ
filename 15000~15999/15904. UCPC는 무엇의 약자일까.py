string = input()
result = ""
flag1, flag2, flag3, flag4 = False, False, False, False

for i in string:
    if "U" == i and not flag1:
        result += i
        flag1 = True
    elif "C" == i and not flag2 and flag1:
        result += i
        flag2 = True
    elif "P" == i and not flag3 and flag1 and flag2:
        result += i
        flag3 = True
    elif "C" == i and not flag4 and flag1 and flag2 and flag3:
        result += i
        flag4 = True


if "UCPC" in result:
    print("I love UCPC")
else:
    print("I hate UCPC")
