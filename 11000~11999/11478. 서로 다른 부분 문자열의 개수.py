S = input()
result = []
for i in range(len(S)):
    for j in range(len(S)+1):
        if S[i:j] != '':
            result.append(S[i:j])

result = set(result)
print(len(result))
