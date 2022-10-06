"""
str - immutable
bool - immutable
int - immutable
float - immutable
list - mutable
"""

# tuple - immutable
# double ctrl
# hold ctrl + down arrow
# ctrl + shift + left arrow
# ctrl + c
# to exit => esc
"""
غیر قابل تغییر
تکراری قبول میکند
المان های داخل به ترتیب است.
"""
# parenthesis
a_tuple1 = (1,)  # tuple
a_tuple2 = (1, 2, 3, 4)
a_tuple3 = (1, 1, 1, 4)  # قبول کردن المان های تکراری
a_tuple4 = (1, 2, 3, 4)

# int, float, str, bool, list
a_tuple5 = tuple(("A", "B"))  # built-in function

# a_tuple2 = (1)  # generator

print(f"a_tuple1: {type(a_tuple1)}, value: {a_tuple1}")
print(f"a_tuple2: {type(a_tuple2)}, value: {a_tuple2}")
print(f"a_tuple3: {type(a_tuple3)}, value: {a_tuple3}")
print(f"a_tuple4: {type(a_tuple4)}, value: {a_tuple4}")

# access to the element with index
print(f"{a_tuple1[0]}")

# TypeError: 'tuple' object does not support item assignment
# a_tuple1[0] = 1
a_list = list(a_tuple1)
a_list.append(5)
print(a_list)

# len()
print(f"len: {len(a_tuple1)}")
