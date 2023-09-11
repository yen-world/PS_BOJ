import sys
input = sys.stdin.readline

card, card_sum = map(int, input().split())

num_list = list(map(int, input().split()))

result = 0
for i in range(len(num_list)-2):
    for j in range(i+1, len(num_list)-1):
        for k in range(j+1, len(num_list)):
            if num_list[i]+num_list[j]+num_list[k] == card_sum:
                result = num_list[i]+num_list[j]+num_list[k]
                break
            elif num_list[i]+num_list[j]+num_list[k] > card_sum:
                continue
            elif num_list[i]+num_list[j]+num_list[k] < card_sum:
                if result < num_list[i]+num_list[j]+num_list[k]:
                    result = num_list[i]+num_list[j]+num_list[k]
                else:
                    continue

print(result)
