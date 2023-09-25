N = int(input())
result = 0

for i in range(N):
    S = input()
    for j in range(len(S) - 1):
        if S[j] == "0" and S[j + 1] == "1":
            result += 1
            break
        elif S[j] == "O" and S[j + 1] == "I":
            result += 1
            break

print(result)
