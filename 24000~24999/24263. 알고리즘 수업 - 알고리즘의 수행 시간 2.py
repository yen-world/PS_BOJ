def MenOfPassion(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt


n = int(input())
result = MenOfPassion(n)
print(result)
print(int(result/n))
