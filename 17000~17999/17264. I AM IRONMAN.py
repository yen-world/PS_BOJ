import sys
input = sys.stdin.readline

n, p = map(int, input().split())
w, l, g = map(int, input().split())
p_dict = dict()
score = 0
g_flag = False

for i in range(p):
    p_name, p_flag = input().rstrip().split()
    p_dict[p_name] = p_flag

for i in range(n):
    p_name = input().rstrip()
    if p_name not in p_dict.keys():
        score -= l
        if score < 0:
            score = 0
    else:
        if p_dict[p_name] == 'W':
            score += w
        else:
            score -= l
            if score < 0:
                score = 0

    if score >= g:
        g_flag = True

if g_flag:
    print("I AM NOT IRONMAN!!")
else:
    print("I AM IRONMAN!!")
