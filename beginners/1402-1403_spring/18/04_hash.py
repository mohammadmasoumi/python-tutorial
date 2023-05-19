# hash

"""
builtin function
 - hash
 - int
 - set
 - float
 - ...
 - print
 - input
 - max
 - min
 - ...

"""


def my_hash(i):
    # run
    # "ali" -> int 02
    # "lia" -> int 03

    # 1 -> 1
    # True -> 1
    # False -> 0


    pass


print(f"{1}: {hash(1)}")
print(f"{True}: {hash(True)}")

print({1, True})
print({True, 1})

radnia = 'radnia'
print(f"{radnia}: {hash(radnia)}")
print(f"{radnia}: {hash(radnia)}")
print(f"{radnia}: {hash(radnia)}")

imani = 'irani'
print(f"{imani}: {hash(imani)}")

my_tuple = (1, 2, 3)
print(f"{my_tuple}: {hash(my_tuple)}")

print(f"Set:{{1, 2, 3}}")

# TypeError: unhashable type: 'list'
# print(f"{(1, 2, 3)}: {hash((1, 2, [1, 2]))}")

# TypeError: unhashable type: 'set'
# print(f"{{1, 2, 3}}: {hash({1, 2, 3})}")

# TypeError: unhashable type: 'list'
# print(f"{[1, 2]}: {hash([1, 2])}")
