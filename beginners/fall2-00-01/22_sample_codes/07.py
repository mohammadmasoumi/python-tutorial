
def get_all_prime(m):
    def is_prime(n):
        prime = True

        for num in range(2, n):
            if n % num == 0:
                prime = False
                break

        return prime

    primes = []
    for num in range(2, m):
        prime = is_prime(num)
        primes.append(num) if prime else None

    return primes


print(get_all_prime(17))
print(get_all_prime(8))
