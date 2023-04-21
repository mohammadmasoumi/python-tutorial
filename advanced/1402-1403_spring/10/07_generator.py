def to_square(numbers):
    return (number**2 for number in numbers)

def to_cube(numbers):
    return (number**3 for number in numbers)

def to_even(numbers):
    return (number for number in numbers if number % 2 == 0)

def to_odd(numbers):
    return (number for number in numbers if number % 2 != 0)

def to_string(numbers):
    return (str(number) for number in numbers)


gen1 = to_string(to_cube(to_square(to_odd(range(20)))))
print(next(gen1))
print(next(gen1))

gen2 = to_string(to_cube(to_square(to_even(range(20)))))
print(next(gen2))
print(next(gen2))
