n = int(input())
record = [input() for _ in range(n)]

# 사전 순으로 정렬 이후, 길이 순으로 정렬
record.sort()
record.sort(key=lambda x: len(x))

boj = []
other = []

for i in range(n):
    if record[i].startswith("boj.kr/") and record[i][7:].isdigit():
        boj.append(record[i])
    else:
        other.append(record[i])

other.extend(boj)

for element in other:
    print(element)
