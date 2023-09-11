score_list = []
for i in range(5):
    score = int(input())
    score_list.append(score if score > 40 else 40)
print(sum(score_list)//5)
