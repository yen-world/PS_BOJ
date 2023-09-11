import sys


def hanoi_tower(disk, A, C, B):
    global count
    if disk == 1:
        way.append(A)
        way.append(C)
        count += 1
        return
    else:
        hanoi_tower(disk-1, A, B, C)
        way.append(A)
        way.append(C)
        count += 1
        hanoi_tower(disk-1, B, C, A)


disk = int(input())
A = 1
B = 2
C = 3
count = 0
way = []

hanoi_tower(disk, A, C, B)
sys.stdout.write(str(count)+'\n')

for i in range(0, len(way), 2):
    for j in range(2):
        sys.stdout.write(str(way[i+j])+' ')
    sys.stdout.write('\n')
