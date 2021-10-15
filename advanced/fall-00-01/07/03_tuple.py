# declaration
# ()

# unchangeable
# ordered
# duplicate is allowed (1, 1, 1) / multicate

# be careful
# a_tuple = (1) generator <class 'int'>
# a_tuple = ('a') generator <class 'str'>

# a_tuple = ('a', )
a_tuple = (1,)
a_list = [1]
# a_tuple1 = tuple()

# print(list('a'))

print(a_tuple)
print(type(a_tuple))


# print(a_tuple1)
# print(type(a_tuple1))

# tuple()
def double(i):
    return int(i) * 2
    # (None, None, None)
    # return None


# def my_double(a, b, c):
#     return a, b, c

# map(a_function, iterable)

# print(tuple(map(double, input().split())))
print(
    tuple(
        map(
            double, input().split()
        )
    )
)

# a = tuple(map(double, input().split()))
# print(tuple(map(tuple, input().split())))
# # print(tuple(map(int, input().split())))
