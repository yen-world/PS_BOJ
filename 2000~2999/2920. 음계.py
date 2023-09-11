scale = list(map(int, input().split()))
jud = 0
for i in range(len(scale)-1):
    if scale[i]+1 == scale[i+1]:
        jud = scale[i+1] - scale[i]
    elif scale[i]-1 == scale[i+1]:
        jud = scale[i+1] - scale[i]
    else:
        jud = 0
        print("mixed")
        break

if jud == 1:
    print("ascending")
elif jud == -1:
    print("descending")
