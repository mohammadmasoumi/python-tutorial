#          default value of z is 10
def my_adder(x, y, z="Hello"):
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    return x + y + z

def test_default_value1(a={'a': 1}, b=[1, 2, 3]):
    print(a)
    print(b)


print(my_adder(12 , 13))
print(my_adder(12 , 13, 11))
test_default_value1()