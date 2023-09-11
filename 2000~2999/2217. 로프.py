import sys
input = sys.stdin.readline

n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

max_value = 0
rope_count = 1

for i in range(len(rope)):
    if max_value < rope[i] * rope_count:
        max_value = rope[i] * rope_count
    rope_count += 1

print(max_value)
