while True:
    count = 0
    sentence = input()
    if sentence == "#":
        break
    else:
        for i in sentence:
            if (
                i == "a"
                or i == "A"
                or i == "e"
                or i == "E"
                or i == "i"
                or i == "I"
                or i == "o"
                or i == "O"
                or i == "u"
                or i == "U"
            ):
                count += 1
        print(count)
