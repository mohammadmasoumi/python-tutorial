"""
datatypes:
list
int
str
float
bool
[tuple]

keywords:
for
def
if
else
"""

# def = 2
# builtin function
# list()

"""
tuple - immutable

1. unchangeable [immutable]
2. ordered => indexing [access]
3. allowed duplication (1, 1, 2)
"""

# list => brackets
# tuple => parenthesis
a_tuple1 = (1, 1, 2, 3)
a_tuple2 = (1)  # this is not a tuple
a_tuple3 = (1,)
a_tuple4 = ("Hello")  # this is not a tuple

a_list1 = [1]

print("a_tuple1: ", type(a_tuple1))
print("a_tuple2: ", type(a_tuple2))
print("a_tuple3: ", type(a_tuple3))
print("a_tuple4: ", type(a_tuple4))
print("a_list1: ", type(a_list1))
