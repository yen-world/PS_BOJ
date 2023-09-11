chat_count = int(input())
result = 0
user_list = []

for i in range(chat_count):
    log = input()
    if log == 'ENTER':
        user_list = set(user_list)
        result += len(user_list)
        user_list = []
    else:
        user_list.append(log)

user_list = set(user_list)
result += len(user_list)
user_list = []

print(result)
