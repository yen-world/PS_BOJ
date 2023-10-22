while True:
    word = input()
    if word == "end":
        break

    flag1, flag2, flag3 = True, True, True

    for char in word:
        if char not in ["a", "e", "i", "o", "u"]:
            flag1 = False
        else:
            flag1 = True
            break

    vowel_count, consonant_count = 0, 0
    for char in word:
        if char in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
            consonant_count = 0
        elif char not in ["a", "e", "i", "o", "u"]:
            consonant_count += 1
            vowel_count = 0

        if vowel_count >= 3 or consonant_count >= 3:
            flag2 = False
            break

    continuous_count = 0
    last_char = word[0]
    for char in word:
        if last_char == char:
            continuous_count += 1
        else:
            last_char = char
            continuous_count = 1

        if continuous_count >= 2 and last_char != "e" and last_char != "o":
            flag3 = False
            break

    if flag1 and flag2 and flag3:
        print("<{}> is acceptable.".format(word))
    else:
        print("<{}> is not acceptable.".format(word))
