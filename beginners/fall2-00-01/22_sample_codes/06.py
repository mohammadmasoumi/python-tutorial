

def is_prime(n):
    prime = True

    for num in range(2, n):
        if n % num == 0:
            prime = False
            break

    return prime


print(is_prime(17))
print(is_prime(8))
