plane = input()
key = input()
cipher = ""

for i in range(len(plane)):
    if plane[i] == " ":
        cipher += " "
        continue

    char_key = ord(key[i % len(key)])
    char_plane = ord(plane[i])

    if char_plane - char_key > 0:
        cipher += chr(char_plane - char_key + 96)
    else:
        cipher += chr(char_plane - char_key + 26 + 96)

print(cipher)
