while True:
    name, age, height = input().split()
    age = int(age)
    height = int(height)
    if name == "#" and age == 0 and height == 0:
        break

    if age > 17 or height >= 80:
        print("{} Senior".format(name))
    else:
        print("{} Junior".format(name))
