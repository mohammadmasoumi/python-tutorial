
# def add(a, b, c):
#     pass

a, *b= 12, 13, 14, 15
# b = [13, 14, 15]

def add(*args):
    print(f"args: {args}, type(args): {type(args)}")
    return sum(args)


print(add())
print(add(10, 11))
print(add(10, 11, 12))
print(add(10, 11, 12, 13))
print(add(10, 11, 12, 13, 14, 15, 16))


# def add(a, b, c):
#     pass

a, *b= 12, 13, 14, 15
# b = [13, 14, 15]

def update(**kwargs):
    print(f"kwargs: {kwargs}, type(kwargs): {type(kwargs)}")
    # return sum(kwargs)

print(update())
update(a=10, b=11)
update(a=10, b=11, c=12)
update(a=10, b=11, c=12, d=13)
update(a=10, b=11, c=12, d=13, e=14, f=15, g=16)

# ---------------------------------------------------------
d1 = {
    "a": 1,
    "b": 2
}

d2 = {
    "c": 1,
    "d": 2
}

print({**d1, **d2})

"""
{
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 2
}
"""

l1 = ["a", "b"]
l2 = ["c", "d"]

print([*l1, *l2])

"""
["a", "b" ,"c" ,"d"]
"""