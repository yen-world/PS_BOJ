import math

ascend_meter, slip_meter, height = map(int, input().split())

days = math.ceil((height - ascend_meter) / (ascend_meter - slip_meter))+1

print(days)
