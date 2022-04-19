# kwargs
# key value args

def add(a, b):
    return a + b

# positional - args
# print(add(12, 13)) # a: 12, b: 13
# -----------------------
# # key value - kwargs
# print(add(a=12, b=13)) # key value, a: 12, b:13
# print(add(b=13, a=12)) # b: 13, a: 12

d1 = {'a': 12, 'b': 13}
d2 = {'c': 14, 'd': 15}

# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(d1 + d2)
# print(d1.update(d2))

# -----------------------
# print(         None         )
# print(     print("Hello")    )
"""
def print(msg):
    # write msg on the terminal
    return None
"""
# a = None
a = print("Hello")
print(f"a: {a}")

# print("Hello")
# print(None)

# def func_unlimited_args(**inputs):
#     print(f"inputs: {inputs}, type: {type(inputs)}")

# func_unlimited_args()
# func_unlimited_args(1, 2, 3, 4, 4)
# func_unlimited_args(1, 2, 3, 4, 4, 5)
# func_unlimited_args(1, 2, 3, 4, 4, 5, 6)