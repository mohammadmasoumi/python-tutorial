n = int(input())

is_prime = True
for number in range(2, n - 1):
    if n % number == 0:
        is_prime = False

print(is_prime)