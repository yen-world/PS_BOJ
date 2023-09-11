import math

N = int(input())
log = int(math.ceil(math.log2(N)))
log2 = log-1
result = int((N - 2**log2) * 2)
print(result)
