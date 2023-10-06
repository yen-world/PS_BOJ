N = input()
dic = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "0": 0}
result = 0

for i in N:
    dic[i] += 1

if dic["6"] or dic["9"]:
    if (dic["6"] + dic["9"]) % 2 == 0:
        dic["6"] = round((dic["6"] + dic["9"]) / 2)
    else:
        dic["6"] = round((dic["6"] + dic["9"]) / 2 + 0.5)

    dic["9"] = dic["6"]

for i in dic.values():
    if result < i:
        result = i

print(result)
