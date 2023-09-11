t = int(input())

for i in range(t) :
    rank = int(input())
    if rank > 4500 :
        print("Case #{}: Round 1".format(i+1))
    elif rank > 1000 :
        print("Case #{}: Round 2".format(i+1))
    elif rank > 25 :
        print("Case #{}: Round 3".format(i+1))
    else :
        print("Case #{}: World Finals".format(i+1))
