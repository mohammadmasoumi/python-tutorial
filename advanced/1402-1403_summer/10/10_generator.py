"""
list comprehension
my_list = [idx for idx in range(10)]
"""

def sequence():
    return (item + 1 for item in range(5))

def double(gen):
    return (item ** 2 for item in gen)

def even(gen):
    return (item for item in gen if item % 2 == 0)

gen = even(double(sequence()))
print(next(gen))
print(next(gen))