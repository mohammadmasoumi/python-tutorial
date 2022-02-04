# functions are first class object in python


def square(x):
    """Square of x."""
    return x*x


def cube(x):
    """Cube of x."""
    return x*x*x


x = 4
square_alternative = square
cube_alternative = cube

print(f"square, square_alternative: {id(square)}, {id(square_alternative)}")
print(f"cube, cube_alternative: {id(cube)}, {id(cube_alternative)}")

print(square(x))
print(square_alternative(x))
print(cube(x))
print(cube_alternative(x))
