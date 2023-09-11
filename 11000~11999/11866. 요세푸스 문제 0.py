import queue

N, K = map(int, input().split())
K = K - 1
M = K
array = queue.Queue()
for i in range(1, N+1):
    array.put(i)
new_array = []

while not array.empty():
    for i in range(K):
        array.put(array.queue[0])
        array.get()
    new_array.append(array.get())

print("<", end='')
print(*new_array, sep=', ', end='')
print(">", end='')
