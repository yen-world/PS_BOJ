def queen(depth):
    global result
    if depth == n :
        result += 1
        return
    
    for i in range(n) :
        if not (matrix[i] or left_diagonal[i+depth] or rigth_digonal[i-depth]) :
            matrix[i] = left_diagonal[i+depth] = rigth_digonal[i-depth] = True
            queen(depth+1)
            matrix[i] = left_diagonal[i+depth] = rigth_digonal[i-depth] = False

n = int(input())
result = 0
matrix = [False] * n
left_diagonal = [False] * (2*n)
rigth_digonal = [False] * (2*n)

queen(0)
print(result)