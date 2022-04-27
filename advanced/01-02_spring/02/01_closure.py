# closure
# wrapper(10)
# def shout():
#     pass
# yell = shout

def multiplier(n):
    # n: 3
    # wrapper has binded to n
    def wrapper(x):
        # x: 10
        return n * x

    return wrapper

# multiply_by_3 = wrapper
multiply_by_3 = multiplier(3)

# wrapper(10)
print(multiply_by_3(10))
print(multiply_by_3(12))
print(multiply_by_3(14))

# binding 
del multiplier

# NameError: name 'multiplier' is not defined
# multiply_by_4 = multiplier(4)

print(multiply_by_3(15))