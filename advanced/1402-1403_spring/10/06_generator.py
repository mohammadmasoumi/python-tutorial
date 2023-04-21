# chain of generator

def square(stop=10):
    # [for ] list comprehension
    return (idx**2 for idx in range(1, stop+1))

def cube(iterator):
    # iterator: square()
    # iterator: generator => square()
    # my_iter = iter(iterator)
    # next(my_iter)
    # next(square())
    return (idx**3 for idx in iterator)

gen = cube(square())
# TypeError: 'generator' object is not callable

# next(cube())
print(next(gen))
print(next(gen))
print(next(gen))

# print(type(gen)) # <class 'generator'>

# print(next(square()))
# print(next(square()))
# print(next(square()))