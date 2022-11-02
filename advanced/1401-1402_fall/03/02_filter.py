my_list = [1, 2, 3, 4]

# Iterable
#  list, set, dict, str

# for character in "Hello":
#     print(character)

"""
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.
"""
# Anonymous
# lambda inputs: output
# b = lambda x: x * 2

# Only one output
# Exception
# b = lambda x, y: x * 2, y * 2

# Many inputs
# b = lambda x, y: y + x * 2

# Accept args
# b = lambda *args: args
# print(b(1, 2))

# Accept kwargs
# b = lambda **kwargs: kwargs
# print(b(a=12, b=13))

# kwargs: {"a": 12} args: (12, )
# kwargs.update(args=args)
# kwargs: {"a": 12, "args": (12, )}
# kwargs[args] = args => kwargs: {"a": 12, "args": (12, ), (12, ): (12, )}
# key =>
# {
#   int
#   str
#   float
#   tuple
#   bool
# }
# [Hashable]
# list, set, dict unhashable
# TypeError: unhashable type: 'list'
# print(hash([12, 13]))
# d = {}

print(hash("asghar"))
print(hash("asghar"))

# def update(key, val
# ue):
#     d[key] = value
#     return None

# c = []
# c.append(12)
# print(c)
# d.update(a=12)
# print(d)

# b = lambda *args, **kwargs: kwargs.update(args=args)
# print(b(12, a=12))


def b(x): return x * 2


print(b(2))


# -----------------
my_list = [1, 2, 3, 4]
print(filter(lambda x: x % 2, my_list))
print(list(filter(lambda x: x % 2, my_list)))
print(set(filter(lambda x: x % 2, my_list)))
print(tuple(filter(lambda x: x % 2, my_list)))
