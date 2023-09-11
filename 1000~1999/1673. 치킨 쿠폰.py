while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break

    result = n
    coupon = n

    while coupon >= k:
        result += coupon // k
        coupon = coupon - (k * (coupon // k)) + (coupon // k)
    print(result)
