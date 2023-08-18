# type

my_list = [1, 1.1, "hello", True]
for item in my_list:
    print(item, type(item))

# ----------------------------
my_list = [int, float, str, bool]
for item in my_list:
    print(item, type(item)) # type


"""
Metaclass

     ---------|
     |        |
     V        |
----------    |  
|  type  | ---|
----------
|       |
int     str

"""

# ----------------------------
print(type(type(int))) # type

# type -> type => type