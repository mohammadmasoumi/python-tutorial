
def factorial(n):
    acc = n

    for num in range(1, n):
        acc *= num

    return acc

print(factorial(5))