def get_two(n):
    two = 2
    count = 0
    while n // two > 0:
        count += n // two
        two *= 2
    return count


def get_five(n):
    five = 5
    count = 0
    while n // five > 0:
        count += n // five
        five *= 5
    return count


n, m = map(int, input().split())

print(min(get_two(n)-get_two(m)-get_two(n-m),
      get_five(n)-get_five(m)-get_five(n-m)))
