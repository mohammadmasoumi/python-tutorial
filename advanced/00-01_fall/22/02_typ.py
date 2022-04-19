"""
int
list
float
str
"""

n = 10
l = [1, 2, 3, 4]
d = {'a': 1, 'b': 2}


# class Foo(object):
class Foo:
    pass


foo = Foo()

for item in (n, l, d, foo):
    print(type(item) is item.__class__)

print(type(str))
print(type(int))
print(type(float))
