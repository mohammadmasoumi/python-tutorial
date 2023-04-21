# Common pitfalls

def generate_square(stop=10):
    for idx in range(1, stop+1):
        yield idx ** 2


print(next(generate_square()))
print(next(generate_square()))
print(next(generate_square()))
print(next(generate_square()))