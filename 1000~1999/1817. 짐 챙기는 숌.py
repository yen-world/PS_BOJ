N, M = map(int, input().split())
if N > 0 :
    books = list(map(int, input().split()))
current_box = 0
box_count = 1

for i in range(N) :
    if books[0] + current_box <= M :
        current_box += books[0]
        books.pop(0)
    else :
        current_box = books[0]
        box_count += 1
        books.pop(0)

print(0 if N == 0 else box_count)