number = int(input())
prime_number = list(map(int, input().split()))
min_prime = min(prime_number)
max_prime = max(prime_number)

print(min_prime * max_prime)
