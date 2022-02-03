from import_me import adder, adder2

# TypeError: adder() takes 0 positional arguments but 2 were given
# print(adder(13, 12)) # you do not have permission to call adder like this

def my_adder(x, y, z):
    """ add 3 numbers
    @param x: 
    

    Args:
        x (int): [number]
        y (int): [number]
        z (int): [number]

    Returns:
        int: sum of 3 numbers
    """
    return adder2(x, b=y, c=z)

print(adder(b=13, a=12))
print(adder2(113, c=12, b=23))
print(adder2(113, b=12, c=23))
print(adder2(a=113, b=12, c=23))
print(adder2(a=113, b=12, c=23))
print(my_adder(x=1, y=2, z=3))